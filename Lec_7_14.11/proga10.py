def add(x,y):
    return x**2 + y**3
# 1200 lines of code


x = lambda a,b: a**2 + b**2 - 2*a*b
print(type(x))
print(x(2,3))
for i in range(10):
    print((lambda x,y: x**2 + y**3)(i,i+1))


