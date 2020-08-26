import clilib.util

logger = clilib.util.get_logger(f"[{__name__}]")


def verb(*args, **kwargs):
    logger.debug('Decorating verb')
    logger.debug(f"args  : {args}")
    logger.debug(f"kwargs: {kwargs}")

    func = args[0]
    logger.debug(f"func  : {func}")
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    action = func.__name__
    logger.debug(f"action: {action}")
    logger.debug(f"Adding attribute '__action={action}' to decorated method")
    setattr(wrapper, '__action', action)

    return wrapper
