#Словарь - множество пар ключ:значение. --------- Хэш-таблица / Ассоциативный массив

my_dict = {}
print(my_dict, type(my_dict))

my_dict = {1:[1,2,3,4], 1.1:(2,3,4), "three":True, False:4, None:1, (1,2,3):11}
print(my_dict)
print(my_dict[1], my_dict[False])
my_dict["six"] = 6
print(my_dict)
print(my_dict[(1,2,3)])

my_dict["six"] = "asdadsf"
print(my_dict)


