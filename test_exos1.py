from exercice1.q1 import get_list_of_random_int
from exercice1.q2 import compare_set
from exercice1.q3 import diff_set
from exercice1.q4 import measure_execution_time
from exercice1.q5 import measure_execution_time_with_average

def main():
    nb_item = 200
    t1 = get_list_of_random_int(nb_item, 1, 10000000)
    t2 = get_list_of_random_int(nb_item, 1, 10000000)
    assert len(t1) == nb_item

    assert type(compare_set(t1, t2)) is tuple

    assert type(diff_set(t1, t2)) is tuple

    assert type(measure_execution_time(1, compare_set, t1, t2)) is float

    assert type(measure_execution_time_with_average(
        1, 10, compare_set, t1, t2
    )) is float


if __name__ == '__main__':
    print("Démarre le script de test !")
    main()
    print("Fin du script de test, tout va bien !")