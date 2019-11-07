def my_add(a, b):
    res = a ** 3 + b**2
    res = res**2
    return res 

my_result = my_add(2, 3)
print(my_result)

# ГЛАВНАЯ ОСОБЕННОСТЬ RPARGS: разработчик должен гарантировать, что между а и b можно выполнить
# все операции внутри тела функции

my_result2 = my_add(2.5, 3.5)
print(my_result2)

my_result3 = my_add(True, False)
print(my_result3)