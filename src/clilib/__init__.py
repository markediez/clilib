import clilib.decorator
import clilib.base
import clilib.util

import argparse

_root_parser = argparse.ArgumentParser()
_subparsers = _root_parser.add_subparsers()
_args = None


def build_parser(parser):
    return parser


def run(prog):
    global _root_parser
    global _args

    _root_parser.prog = prog
    _args = _root_parser.parse_args()
