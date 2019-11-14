def add(a,b):
    return a + b

def mult(a,b):
    print(a * b)
    #return None


mult(4,5)

def with_default(a = 1, b = 2):
    return a + b

with_default(1)
with_default(b = 1,a = 33)
with_default()