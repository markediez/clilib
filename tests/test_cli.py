import clilib


@clilib.decorator.resource
class MyResource():
    @clilib.decorator.verb
    def get(self):
        print("get MyResource")


@clilib.decorator.resource
class OtherResource():
    @clilib.decorator.verb
    def get(self):
        print("get OtherResource")


@clilib.decorator.resource
class FooResource():
    @clilib.decorator.verb
    def list(self):
        print("list FooResource")


class TestCli:
    def test_parser_prog_name_is_value_passed(self):
        clilib.run("clilib")
        assert clilib._root_parser.prog == "clilib"

    def test_parsed_args_has_default_func_attribute_to_run(self):
        args = clilib._root_parser.parse_args([
            "list",
            "foo-resource"
        ])
        assert hasattr(args, '_func')

    def test_list_foo_resource(self):
        args = clilib._root_parser.parse_args([
            "list",
            "foo-resource"
        ])
        assert(args._func == FooResource.list)

    def test_same_verb_for_multiple_resource(self):
        args = clilib._root_parser.parse_args([
            "get",
            "my-resource"
        ])
        assert(args._func == MyResource.get)

        args = clilib._root_parser.parse_args([
            "get",
            "other-resource"
        ])
        assert(args._func == OtherResource.get)
