from celery import Celery
from celery.schedules import schedule   
from datetime import timedelta
from functools import cached_property
import logging

def tasks_save_results(x):
    if x[1]['logged'] is True:
        return x

def relaunchable(x):
    if x[1]['user_retry'] is True:
        return x
    
def crontab(**args):
    return schedule(timedelta(**args))

@cached_property
def relaunchable_tasks():
    return filter(relaunchable, Config.beat_schedule.items())

@cached_property
def relaunchable_tasks():
    return filter(tasks_save_results, Config.beat_schedule.items())

class Config:

    beat_schedule = {
        'task_title': {
            'task':'tasks.task_route',
            'schedule':crontab(seconds=30),
            #'user_retry':True,
            #'logged':True
        },
        'task_title_2': {
            'task':'tasks.task_route_2',
            'schedule':crontab(seconds=30),
            #'user_retry':False,
            #'logged':True
        },
    }


    timezone = 'UTC'
    celery_queues = {
        'high_priority': {
            'exchange': 'high_priority',
            'routing_key': 'high_priority',
            'priority': 10,
        },
        'default': {
            'exchange': 'default',
            'routing_key': 'default',
            'priority': 5,
        },
        'low_priority': {
            'exchange': 'low_priority',
            'routing_key': 'low_priority',
            'priority': 1,
        },
    }

def make_celery(app):

    """
    Sirve para la creación de la cola de peticiones de celery.
    :param app: Aplicación Flask.
    :type app: Flask Application.
    :return: cola de tareas Celery.
    :rtype: Celery Object.
    """
    celery = Celery(
        app,
        backend='redis://localhost:6379/0',
        broker='redis://localhost:6379/0'
    )

    celery.config_from_object(Config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            logging.info("Executing task!")
            return self.run(*args, **kwargs)
    celery.Task = ContextTask
    
    return celery