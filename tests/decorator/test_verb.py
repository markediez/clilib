from clilib.decorator.resource import resource
from clilib.decorator.verb import verb

class TestDecoratorVerb():
    def test_decorated_function_registers_as_a_verb(self):
        @resource
        class MyResource():
            @verb
            def get(self):
                print("Got something")

        assert 'get' in getattr(MyResource, '__parsers')


    def test_specify_verb_through_decorator(self):
        pass

