from clilib.decorator import resource, verb

class TestDecoratorVerb():
    def test_decorated_function_registers_as_a_verb(self):
        @resource
        class MyResource():
            @verb
            def get(self):
                print("Got something")

        # Need to run the function for decorators to compile
        # TODO: Figure out a way to not do this... check Flask code?
        MyResource().get()
        assert 'get' in getattr(MyResource, '__parsers')


    def test_specify_verb_through_decorator(self):
        pass

