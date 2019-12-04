def worker(a :int):
    assert (a < 30), "Value cannot be > 30"
    print("COOL!")

try:
    A = 32
    worker(A)
    print(1 / 0)
    
except AssertionError as a_err:
    print("error happend: ",a_err)
except ZeroDivisionError as z_err:
    print("error happend:",z_err)


print("GRACEFUL SHUTDOWN ")