def add(a :int, b :int) -> int:
    return a + b + 1
    
def sub(a :int, b :int) -> int:
    return a - b 

def mult(a :int, b :int) -> int:
    return a * b 

def div(a:int, b:int) -> float:
    if ( b != 0):
        return a / b 
    else:
        return 0
a = 109
print("Hi from another module!")


class User:
    def __init__(self):
        self.a = "a"