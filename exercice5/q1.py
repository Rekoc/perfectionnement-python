import random
from multiprocessing import Process, Queue
from exercice1.q1 import get_list_of_random_int


def queueing_result(x: int, q: Queue, *args):
    for i in range(x):
        # for item in get_list_of_random_int(*args):
        #    q.put(item)
        q.put(get_list_of_random_int(*args))

def start_processus(*args):
    queue = Queue()
    proc = Process(target=queueing_result, args=(
        random.randint(1, 5), queue, *args,
    ))

    proc.start()
    proc.join()

    size = queue.qsize()
    while not queue.empty():
        print(f"- item n°{size - queue.qsize()} : {queue.get()}")