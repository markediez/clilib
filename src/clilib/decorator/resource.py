import clilib
from . import verb

def resource(klass):
    setattr(klass, '__parsers', {})
    setattr(klass, '__name', '')

    for key, value in klass.__dict__.items():
        if callable(value) and verb.is_verb(value):
            clilib.register_verb(klass, value)


    return klass
