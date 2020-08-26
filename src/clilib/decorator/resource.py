def resource(klass):
    print("DECORATING RSRC")
    setattr(klass, '__parsers', {})
    setattr(klass, '__name', '')

    for key, value in klass.__dict__.items():
        print(f"Checking '{key}'")
        if callable(value):
            print('Function found. Adding attr')
            setattr(value, '__resource', klass)

    return klass
