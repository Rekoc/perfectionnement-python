from exercice1.q1 import get_list_of_random_int
from exercice1.q2 import compare_set
from exercice1.q3 import diff_set
from exercice1.q4 import measure_execution_time
from exercice1.q5 import measure_execution_time_with_average
from pprint import pprint


def main():
    print("\n# Question 1 :")
    t1 = get_list_of_random_int(200000, 1, 10000000)
    t2 = get_list_of_random_int(50, 1, 10000000)
    pprint(t2, compact=True, underscore_numbers=True)
    # Too much value
    # pprint(t1, compact=True, underscore_numbers=True)

    print("\n# Question 2 :")
    result = compare_set(t1, t2)
    pprint(result)

    print("\n# Question 3 :")
    result = diff_set(t1, t2)
    # Too much value
    # pprint(result, compact=True, underscore_numbers=True)
    print(f"Nombre de diff entre t1 et t2 : {len(result)}")

    print("\n# Question 4 :")
    nb_run = 1
    result = measure_execution_time(nb_run, compare_set, t1, t2)
    print(f"compare_set * {nb_run} --> {result} secondes")
    result = measure_execution_time(nb_run, diff_set, t1, t2)
    print(f"diff_set * {nb_run}    --> {result} secondes")

    print("\n# Question 5 :")
    nb_val = 10
    result = measure_execution_time_with_average(
        nb_run, nb_val, compare_set, t1, t2
    )
    print(f"compare_set * {nb_run} * {nb_val} --> {result} secondes")
    result = measure_execution_time_with_average(
        nb_run, nb_val, diff_set, t1, t2
    )
    print(f"diff_set * {nb_run} * {nb_val} --> {result} secondes")


if __name__ == '__main__':
    main()