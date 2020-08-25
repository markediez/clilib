def resource(klass):
    def wrapper():
        setattr(klass, '__parsers', {})
        setattr(klass, '__name', '')

        return klass

    return wrapper()
