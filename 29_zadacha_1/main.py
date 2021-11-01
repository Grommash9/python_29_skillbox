import functools
from collections.abc import Callable


def check_permission(permissions: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            if permissions in user_permissions:
                results = func(*args, **kwargs)
            else:
                print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию add_comment')
                results = None
            return results
        return wrapped
    return decorator



user_permissions = ['admin']


@check_permission(permissions='admin')
def delete_site():
    print('Удаляем сайт')


@check_permission(permissions='user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
