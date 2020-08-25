import clilib

def verb(func):
    def wrapper(*args, **kwargs):
        resource = args[0]
        clilib.register_verb(resource, func)

        return func(*args, **kwargs)

    return wrapper
