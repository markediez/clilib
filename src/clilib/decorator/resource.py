def resource(klass):
    def wrapper():
        setattr(klass, '__parser', None)
        setattr(klass, '__name', '')
        setattr(klass, '__verbs', [])

        return klass

    return wrapper()