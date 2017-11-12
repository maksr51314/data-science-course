def log(func):
    def wrapper(*a, **kw):
        print(func.__name__)
        print(*a, **kw)
        print(func(*a, **kw))
        return func(*a, **kw)
    return wrapper


@log
def myFunction(a,b):
    return 'some text'


