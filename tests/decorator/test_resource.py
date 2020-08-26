from clilib.decorator import resource

class TestDecoratorResource():
    def test_decorated_class_gets_base_attrs(self):
        @resource
        class MyResource():
            someattr = 'attr'

        assert MyResource.someattr == 'attr'
        assert hasattr(MyResource, '__parsers')
        assert hasattr(MyResource, '__name')


    def test_decorated_class_methods_gets_resource_attribute(self):
        @resource
        class MyResource():
            def get(self):
                print("some func")

        assert hasattr(MyResource.get, '__resource')
        assert getattr(MyResource.get, '__resource') is MyResource