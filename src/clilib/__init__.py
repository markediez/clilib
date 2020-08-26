import clilib.decorator
import clilib.base
import clilib.util

import argparse

_root_parser = argparse.ArgumentParser()
_subparsers = _root_parser.add_subparsers()
_args = None


def build_parser(parser):
    return parser


def register_verb(resource, func):
    resource_name = clilib.util.to_kebab(resource.__name__)
    verb = getattr(func, '__action')

    if verb not in _subparsers.choices:
        _subparsers.add_parser(verb)

    if verb not in resource.__parsers:
        resource.__parsers[verb] = _subparsers.choices[verb].add_subparsers()

    if resource_name not in resource.__parsers[verb].choices:
        resource_parser = resource.__parsers[verb].add_parser(resource_name)
        resource_parser.set_defaults(func = func)


def run(prog):
    global _root_parser
    global _args
    global _subparsers

    _root_parser.prog = prog
    _args = _root_parser.parse_args()

    if hasattr(_args, "func"):
        _args.func(_args)
