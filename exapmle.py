import os,sys

def bad_function(  x ):
    unused_var = 10
    y=20
    return +y

class BadClass:
    def __init__(self):
        pass
    
    def method_one(self,):
        print("method one")
    
    def MethodTwo(self):
        print(method two")

if __name__ == "__main__":
    result = bad_function(5)
    print(f"Result: {result}")
