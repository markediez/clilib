import clilib.decorator.resource as resource
import clilib.decorator.verb as verb
import clilib.decorator.arg as arg


@resource
@arg('--environment', '-e', type=str, default='dev')
class ArgTestResource():
    @verb
    @arg('positional_foo', type=str, default='')
    def get(self, args):
        print("Got something")


class TestDecoratorArg():
    def test_decorated_function_adds_arg(self):
        assert hasattr(ArgTestResource.get, '_args')

    def test_decorated_resource_adds_arg(self):
        assert hasattr(ArgTestResource, '_args')
