temp = 21

print("Больше?", temp > 10)
print("Меньше?", temp < 100)
print("Больше или равно?", temp >= 21)
print("Меньше или равно?", temp <= 10)
print("Равно ли?", temp == 10)
print("Не равно ли?", temp != 10)


print( temp > 10 and temp < 30)
print( temp > 100 or temp < 20)

print("########### Таблица Истинности ############")
print("Логическое И") # Логическое умножение
print(True and True)  # 1 * 1 = 1
print(False and True)  # 0 * 1 = 0
print(True and False) # 1 * 0 = 0
print(False and False) # 0 * 0 = 0

print("Логическое ИЛИ") # Логическое slozheny
print(True or True) # 1 + 1 = 1
print(False or True) # 0 + 1 = 1
print(True or False) # 1 + 0 = 1
print(False or False) # 0 + 0 = 0