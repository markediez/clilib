import clilib.util
from . import verb


logger = clilib.util.get_logger(f"[{__name__}]")

def resource(klass):
    logger.debug(f"class: {klass}")

    logger.debug("Adding attributes '__parsers' and '__name'")
    setattr(klass, '__parsers', {})
    setattr(klass, '__name', '')

    logger.debug(f"Finding verb decorated functions in {klass}")
    for key, value in klass.__dict__.items():
        logger.debug(f"Checking {key}")
        if callable(value) and verb.is_verb(value):
            logger.debug(f"{key} is decorated!")
            clilib.register_verb(klass, value)


    return klass
