# Это пример файла с проблемами для Ruff

def bad_function(  x,y  ):
    unused_var = 10
    result = x + y
    return result

def another_function():
    import sys, os  # Multiple imports on one line
    x=1
    y=2
    return x+y

class TestClass():
    def __init__(self):
        pass
