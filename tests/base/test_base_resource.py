import pytest
import argparse
import clilib.base
from abc import ABC

class Foo(clilib.base.BaseResource):
        pass


def test_base_resource_is_abc():
    assert(issubclass(clilib.base.BaseResource, ABC))


def test_subclass_inherits_properties():
    foo = Foo()

    assert(foo.parser == None)
    assert(isinstance(foo.name, str) and foo.name == "")
    assert(isinstance(foo.verbs, list) and len(foo.verbs) == 0)


def test_subclass_property_types_are_defined():
    foo = Foo()
    
    foo.parser = argparse.ArgumentParser()
    assert(isinstance(foo.parser, argparse.ArgumentParser))

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    foo.parser = subparsers.add_parser('foo')
    assert(isinstance(foo.parser, argparse.ArgumentParser))

    with pytest.raises(AssertionError):
        foo.parser = "assert fail"

    foo.name = "foo"
    assert(foo.name == "foo")    
    with pytest.raises(AssertionError):
        foo.name = 1
    
    foo.verbs = ["a"]
    assert(len(foo.verbs) == 1 and foo.verbs[0] == "a")
    with pytest.raises(AssertionError):
        foo.verbs = "assert fail"


def test_subclass_properties_are_deletable():
    foo = Foo()

    del foo.parser
    assert(not hasattr(foo, "parser"))

    del foo.name
    assert(not hasattr(foo, "name"))

    del foo.verbs
    assert(not hasattr(foo, "verbs"))