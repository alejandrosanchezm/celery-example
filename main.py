from fastapi import FastAPI
from celery_utils import make_celery

app = FastAPI()
celery = make_celery(app)

@celery.task(queue='high_priority',max_retries=2)
def task_route_2():
    print("HOLA 2")

@celery.task(queue='low_priority')
def task_route():
    print("HOLA")    

@app.get('/task1')
def index():
    task_route.delay()
    return "Enqueue task 1!"

@app.get('/task2')
def index():
    task_route_2.apply_async(countdown=10)
    return "Enqueue task 2 with delay of 10 secs!"
