from clilib.decorator import resource

class TestDecoratorResource():
    def test_decorated_class_gets_base_attrs(self):
        @resource
        class MyResource():
            someattr = 'attr'

        assert MyResource.someattr == 'attr'
        assert hasattr(MyResource, '__parser')
        assert hasattr(MyResource, '__verbs')
        assert hasattr(MyResource, '__name')