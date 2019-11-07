def func(a):
    print(a)
    #return None

def another_func():
    print(2 + 3)
    return 5

result = func("Hello")
print(result)

# 1 - ая фишка. Функции в питоне всегда что-то возвращают.
# При наличии return .... в случае остутствия - return None

q = another_func()
print(q)

# 2-ая фишка. У функций может и не быть аргументов.