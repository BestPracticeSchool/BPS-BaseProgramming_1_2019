def my_mult(e, a = 1,b = 3,c =2, d = 1):
    result = a**2 + b**2 + c**2 + d/(a*b*c*d**3)
    return result 

print(my_mult(1,2,3,4))
print(my_mult(2, b = 1, a = 2, d = 3))
print(my_mult(1,2))
print(my_mult(1))
print(my_mult(2))