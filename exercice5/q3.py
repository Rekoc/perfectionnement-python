import random
from celery import Celery
from celery.result import AsyncResult
from exercice1.q1 import get_list_of_random_int


app = Celery("q3", broker="redis://0.0.0.0:6379", backend="redis://0.0.0.0:6379")


@app.task
def hello():
    return "hello world"

@app.task
def start_multiple_processus_celery(x: int, r_min: int, r_max: int):
    return [get_list_of_random_int(x, r_min, r_max) for i in range(x)]

def get_result_by_id(id: str):
    res = AsyncResult(id, app=app)
    if res.state == "SUCCESS":
        return res.get()
    return None