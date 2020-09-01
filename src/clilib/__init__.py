import clilib.util
import clilib.decorator as decorator
import argparse
import logging


_root_parser = argparse.ArgumentParser()
_subparsers = _root_parser.add_subparsers(dest='_cmd')
_subparsers.required = True
_args = None

logger = clilib.util.get_logger(f"[{__name__}]")


def build_parser(parser):
    return parser


def register_verb(resource, func):
    logger.debug('Registering resource verb')

    resource_name = clilib.util.to_kebab(resource.__name__)
    verb = getattr(func, '__action')

    logger.debug(f"resource: {resource}")
    logger.debug(f"func    : {func}")
    logger.debug(f"verb    : {verb}")

    if verb not in _subparsers.choices:
        logger.debug(f"Adding verb, '{verb}', in _subparsers")
        _subparsers.add_parser(verb)

    if verb not in resource.__parsers:
        logger.debug(f"Adding verb, '{verb}', in resource.__parsers")
        if verb in _subparsers.choices:
            logger.debug(f"Referencing subparser of _subparsers.choices['{verb}']")
            resource.__parsers[verb] = clilib.util.get_subparser(_subparsers.choices[verb])
        else:
            logger.debug(f"Creating _subparsers.choices['{verb}']")
            resource.__parsers[verb] = _subparsers.choices[verb].add_subparsers()

    if resource_name not in resource.__parsers[verb].choices:
        logger.debug(f"Adding resource, {resource}, target for verb, {verb}, as {resource_name}")
        resource_parser = resource.__parsers[verb].add_parser(resource_name)
        resource_parser.set_defaults(_func=func)


def init(prog):
    global _root_parser

    _root_parser.prog = prog


def run(prog):
    global _root_parser
    global _args
    global _subparsers

    _root_parser.prog = prog
    _args = _root_parser.parse_args()

    if hasattr(_args, "_func"):
        _args._func(_args)
