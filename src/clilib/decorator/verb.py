import clilib

SUBPARSERS = {}

def verb(verb):
    def _verb(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        if verb not in clilib._subparsers.choices:
            clilib._subparsers.add_parser(verb)

        if verb not in SUBPARSERS:
            SUBPARSERS[verb] = clilib._subparsers.choices[verb].add_subparsers()

        resource_name = clilib.util.to_kebab(clilib.util.get_resource_name(func))
        if resource_name not in SUBPARSERS[verb].choices:
            resource_parser = SUBPARSERS[verb].add_parser(resource_name)
            resource_parser.set_defaults(func=func)

        return wrapper

    return _verb