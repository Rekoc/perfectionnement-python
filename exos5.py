import time
from pprint import pprint
from exercice5.q1 import start_processus
from exercice5.q2 import start_multiple_processus
from exercice5.q3 import get_result_by_id, start_multiple_processus_celery


def main():
    print("\n# Question 1 :")
    start_processus(5, 1, 10_000_000)

    print("\n# Question 2 :")
    start_multiple_processus(10, 5, 1, 10_000_000)

    # To start Celery and Redis database :
    # docker run -d -p 6379:6379 redis
    # python -m celery -A exercice5.q3 worker --loglevel=INFO
    print("\n# Question 3 :")
    ids = []
    for i in range(10):
        ids.append(
            start_multiple_processus_celery.delay(5, 1, 10_000_000).id
        )
    time.sleep(3)
    results = []
    for id in ids:
        tmp = get_result_by_id(id)
        for item in tmp:
            results.append(item)
    pprint(results)


if __name__ == '__main__':
    main()