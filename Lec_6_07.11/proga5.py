def factorial(n):
    n = abs(n)
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1,n+1):
            result *= i
        return result


# n! = n * (n -1) * (n - 2) * ... * 1
# 2! = 2 * 1
# 3! = 3 * 2 * 1
# 1! = 1
# 0! = 1

for i in range(-20, 20):
    print(i, "factor is",factorial(i))
print("ALLES!")

# n!! = (n!)!
# 2!! = (2!)! = 2!= 2
# 3!! = (3!)! = 6! = 720
print("#######################")
for i in range(0, 10):
    print(i,"double factor is", factorial(factorial(i)))
print("ALLES!")