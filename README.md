# clilib
Python Library to create CLI tools using Subject-Verb-Object pattern
```
my-cmd [my-namespace] my-action my-resource [pos_args] [--options]
```

# Quickstart 1: CLI without Namespaces
1. `pip install clilib`
2. Create a hello world CLI
```python
import clilib

@clilib.Resource
class MyResource():
    def get(self):
        print "Hello world"

clilib.run("mycli")
```
3. Run your program
```
$ python example.py get my-resource
Hello world
```

# Quickstart 1: CLI with Namespaces
1. `pip install clilib`
2. Create the runner, `example.py`
```python
import clilib

clilib.run("mycli")
```
3. Namespaces are sub-packages of an expected local `namespace` package
```
$ mkdir -p namespace namespace/my-namespace
$ touch namespace/__init__.py namespace/my-namespace/__init__.py
```
```python
# namespace/my-namespace/__init__.py
import clilib

@clilib.Resource
class MyResource():
    def get(self):
        print("Hello World")
```
4. Run your program
```
$ python example.py my-namespace get my-resource
Hello World
```

# Decorators

# Notes
- You can either have `cli namespace action resource` **OR** `cli action resource`

# Roadmap
- [ ] Global Config -- [Potential](https://docs.python.org/3.2/library/argparse.html#the-namespace-object)

# Testing
- flake8
- pytest
- pylogrus