from exercice2.q1 import log_execution_time
from exercice2.q2 import trigger as trigger_q2
from exercice2.q3 import event
from exercice2.q_bonus import log_execution_time_with_path
from pathlib import Path

@log_execution_time
def random_method(nb: int):
    for i in range(nb):
        pass

BASE_DIR = Path(__file__).resolve().parent
@log_execution_time_with_path(f"{BASE_DIR}/statics/exercice1_q_bonus.txt")
def random_method2(nb: int):
    for i in range(nb):
        pass

def main():
    print("\n# Question 1 :")
    random_method(10_000_000)

    print("\n# Question 2 :")
    trigger_q2('evenement1')
    trigger_q2('evenement2')

    print("\n# Question 3 :")
    event.trigger('evenement1')
    event.trigger('evenement2')

    print("\n# Question Bonus :")
    random_method2(10_000_000)


if __name__ == '__main__':
    main()