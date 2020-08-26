import clilib.decorator.resource as resource

class TestDecoratorResource():
    def test_decorated_class_gets_base_attrs(self):
        @resource
        class MyResource():
            someattr = 'attr'

        assert MyResource.someattr == 'attr'
        assert hasattr(MyResource, '__parsers')
        assert hasattr(MyResource, '__name')
