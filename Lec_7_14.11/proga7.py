def metric(*args:int) -> int:
    summ = 0
    for i in args:
        summ += i**2
    return summ

print(metric(1,2,3,4,5,6,7,10))
print(metric(3,4))
print(metric(123,123,1235234))
print(metric(8))