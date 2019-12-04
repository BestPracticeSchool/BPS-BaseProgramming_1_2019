def worker(a :int):
    assert (a < 30), "Value cannot be > 30"
    #print("COOL!")

try:
    A = 31
    worker(A)
    #print(1 / 0)
    
except AssertionError as a_err:
    print("error happend: ",a_err)
except ZeroDivisionError as z_err:
    print("error happend:",z_err)
else:
    print("No errors happend")
finally:
    print("FINALLY!!!!")

print("GRACEFUL SHUTDOWN ")