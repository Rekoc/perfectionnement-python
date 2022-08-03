import random
from multiprocessing import Pool, Manager
from exercice1.q1 import get_list_of_random_int


def queueing_result(x: int, q, *args):
    for i in range(x):
        # for item in get_list_of_random_int(*args):
        #    q.put(item)
        q.put(get_list_of_random_int(*args))

def start_multiple_processus(nb_proc: int, *args):
    pool = Pool(nb_proc)
    manager = Manager()
    shared_queue = manager.Queue()

    for i in range(nb_proc):
        pool.apply_async(queueing_result, args=(
            random.randint(1, 5), shared_queue, *args,
        ))

    pool.close()
    pool.join()

    size = shared_queue.qsize()
    while not shared_queue.empty():
        print(f"- item n°{size - shared_queue.qsize()} : {shared_queue.get()}")