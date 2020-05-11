import clilib.base

def test_base_resource_is_abc():
    class Foo(clilib.base.BaseResource):
        pass

    assert(issubclass(Foo, clilib.base.BaseResource))


def test_subclass_inherits_parser():
    class Foo(clilib.base.BaseResource):
        pass

    a = Foo("parser")
    assert(a.parser == "parser")

    a.parser = "modify"
    assert(a.parser == "modify")

    del a.parser
    assert(hasattr(a, "parser") == False)

