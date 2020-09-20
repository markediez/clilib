import clilib.decorator.resource as resource
import clilib.decorator.verb as verb
import clilib.decorator.arg as arg


class TestDecoratorArg():
    def test_decorated_function_adds_arg(self):
        @arg('--environment', '-e', type=str, default='dev')
        @resource
        class ArgTestResource():
            @arg('positional_foo', type=str, default='')
            @verb
            def get(self, args):
                print("Got something")
                print(f"positional foo: {args._positional_foo}")

        assert hasattr(ArgTestResource.get, '_args')
        assert hasattr(ArgTestResource, '_args')

    def test_positional_arg_exists(self):
        pass

    def test_flagged_arg_exists(self):
        pass

    def test_multiple_args_exists(self):
        pass

    def test_decorator_as_class_adds_arg_to_all(self):
        pass
