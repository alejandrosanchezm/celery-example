from main import celery
from celery_utils import Config

@celery.task(queue='high_priority',max_retries=2)
def task_route_2():
    print("HOLA 2")

@celery.task(queue='low_priority')
def task_route():
    print("HOLA")    