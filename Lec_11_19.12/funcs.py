# Module -  любой файл с расширением .py
def add(a:int, b:int) -> int:
    return a**2 + b**2 - 2*a*b

def sub(a:int, b:int) -> int:
    return a**2 - b**2 + 2*a*b

def mult(a:int, b:int) -> int:
    return (a - b) * (a + b) * (a*b)

def div(a:int, b:int) -> float:
    return a / b - b / a 



print("Module funcs.py started")
print("Module funcs.py finished!")