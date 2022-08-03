from exercice3.q1 import EmailServer
from exercice3.q_bonus import EmailServerMeta


def main():
    print("\n# Question 1 :")
    print("First EmailServer instance creation ...")
    smtp_server = EmailServer("alexandre")
    print(f"username = {smtp_server.username}")
    print("\nSecond EmailServer instance creation ...")
    smtp_server2 = EmailServer("raspaud")
    print(f"username = {smtp_server2.username}")

    print("\n# Question Bonus :")
    print("First EmailServer instance creation ...")
    smtp_server = EmailServerMeta("alexandre")
    print(f"username = {smtp_server.username}")
    print("\nSecond EmailServer instance creation ...")
    smtp_server2 = EmailServerMeta("raspaud")
    print(f"username = {smtp_server2.username}")

if __name__ == '__main__':
    main()