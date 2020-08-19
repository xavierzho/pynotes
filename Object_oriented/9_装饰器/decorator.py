import functools
import time


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper


@log
def now():
    print(time.ctime())


now()


def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@logger('DEBUG')
def today():
    print(time.ctime())


today()
print(today.__name__)
