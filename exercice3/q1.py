class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            print("First time we are calling Singleton !")
            cls.__instance = super().__new__(cls)
        else:
            print("NOT the first time we are calling MetaSingleton !")
        return cls.__instance


class EmailServer(Singleton):
    username = None

    def __init__(self, username: str, *args, **kwargs):
        if self.username is None:
            self.username = username
        print(f"EmailServer __init__ operator called. Ready to be used with username = {self.username}")

    def send_email(self, *args, **kwargs):
        ...