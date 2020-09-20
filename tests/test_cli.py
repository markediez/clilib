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


@clilib.decorator.resource
@clilib.decorator.arg('--dry-run', action='store_true')
@clilib.decorator.arg('--environment', '-e', type=str, choices=['dev', 'uat', 'stage', 'prod'])
class ArgResource():
    @clilib.decorator.verb
    @clilib.decorator.arg('pos_arg', type=str)
    def get(self, args):
        print(f"get ArgResource {args.pos_arg}")

    @clilib.decorator.verb
    def list(self, args):
        print(f"list ArgResource dry_run {args.dry_run} and env {args.environment}")


class TestCli:
    def test_parser_prog_name_is_value_passed(self):
        clilib.init("clilib")
        assert clilib._root_parser.prog == "clilib"

    def test_parsed_args_has_default_func_attribute_to_run(self):
        args = clilib._root_parser.parse_args([
            "list",
            "foo-resource"
        ])
        assert hasattr(args, '_func')

    def test_parsed_args_has_default_klass_attribute_to_pass(self):
        args = clilib._root_parser.parse_args([
            "list",
            "foo-resource"
        ])
        assert hasattr(args, '_klass')

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

    def test_positional_arg_exists(self):
        args = clilib._root_parser.parse_args([
            "get",
            "arg-resource",
            "pug"
        ])

        assert hasattr(args, 'pos_arg')
        assert args.pos_arg == 'pug'

    def test_decorator_as_class_adds_arg_to_all(self):
        args = clilib._root_parser.parse_args([
            "get",
            "arg-resource",
            "pug",
            "--environment",
            "dev"
        ])

        args2 = clilib._root_parser.parse_args([
            "list",
            "arg-resource",
            "--environment",
            "uat"
        ])

        assert hasattr(args, 'environment')
        assert hasattr(args2, 'environment')
        assert args.environment == 'dev'
        assert args2.environment == 'uat'

    def test_multiple_args(self):
        args = clilib._root_parser.parse_args([
            "list",
            "arg-resource",
            "--environment",
            "uat",
            "--dry-run"
        ])

        assert hasattr(args, "environment")
        assert hasattr(args, "dry_run")
        assert args.environment == 'uat'
        assert args.dry_run
