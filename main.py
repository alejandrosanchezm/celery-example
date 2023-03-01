from fastapi import FastAPI
from celery_utils import make_celery, Config, relaunchable_tasks
import logging

app = FastAPI()

celery = make_celery(app)


@app.get('/')
def index():
    return relaunchable_tasks