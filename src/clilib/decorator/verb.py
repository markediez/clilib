def is_verb(func):
    return hasattr(func, '__action')


def verb(*args, **kwargs):
    func = args[0]
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    action = func.__name__
    setattr(wrapper, '__action', action)

    return wrapper
