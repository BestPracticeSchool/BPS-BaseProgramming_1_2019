def add(a:int, b:int) -> int:
    return a + b

def sub(a :int, b : int) -> int:
    return a - b


print(type( add(2,3) ))
print(type( add ))
print(dir( add ))

func_list = [add, sub]
func_list.sort()

print(func_list)
for f in func_list:
    print(f(3,4))

a = add

# Функции в питоне являются объектами первого рода!