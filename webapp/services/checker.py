from flask import session

from functools import wraps


def check_logged_in(func: 'func') -> 'wrapper':
    @wraps(func)  # розібратись навіщо це треба!!!
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in'
    return wrapper