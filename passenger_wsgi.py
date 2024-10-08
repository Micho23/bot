import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

wsgi = load_module('wsgi', 'app.py')
application = wsgi.app