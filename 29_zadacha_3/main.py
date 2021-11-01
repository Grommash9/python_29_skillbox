import functools
from collections.abc import Callable


def singleton(cls) -> Callable:
    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print('создан экземпляр класса')
        return instance

    return wrapped()


@singleton()
class Example:
    def __init__(self, numbers):
        self.numbers = numbers

a = Example(numbers = 2)

