class MetaSingleton(type):
    __instance = None

    def __init__(self, name, bases, dic):
        super().__init__(name, bases, dic)

    def __call__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance

        single_obj = cls.__new__(cls)
        single_obj.__init__(*args, **kwargs)
        cls.__instance = single_obj
        return single_obj


class EmailServerMeta(metaclass=MetaSingleton):
    username = None

    def __init__(self, username: str, *args, **kwargs):
        self.username = username
        print(f"EmailServer __init__ operator called. Ready to be used with username = {self.username}")

    def send_email(self, *args, **kwargs):
        ...