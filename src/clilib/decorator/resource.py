def resource(klass):
    print("DECORATING RSRC")
    setattr(klass, '__parsers', {})
    setattr(klass, '__name', '')

        return klass

    return klass
