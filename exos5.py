from exercice5.q1 import start_processus
from exercice5.q2 import start_multiple_processus

def main():
    print("\n# Question 1 :")
    start_processus(5, 1, 10_000_000)

    print("\n# Question 2 :")
    start_multiple_processus(10, 5, 1, 10_000_000)

    print("\n# Question 3 :")
    


if __name__ == '__main__':
    main()