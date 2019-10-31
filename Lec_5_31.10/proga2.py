# Множества set()
# Словарь dict()

names = ["Sergey", "Nina", "Alex", "Joe", "Joe", "Tomas", "Sergey", "Anna"]
for name in names:
    if names.count(name) >= 2:
        pass
       
#Множество в Python - неиндексируемая коллекция, состоящая из УНИКАЛЬНЫХ элементов.

my_set = set() 
print(my_set, type(my_set))
my_new_set = set([1,2,3,4,5,6,123,1,3,2,5])
print(my_new_set)
print("######################")
print(dir(my_new_set))
#print(my_new_set[-1])
my_new_set.add(-20)
my_new_set.add(-300)
my_new_set.add(-20)
my_new_set.pop()
my_new_set.remove(-20)
print(my_new_set)
print( -300 in my_new_set)

#math
#[1,2,3,4] U [3,4,5,6] = [1,2,3,4,5,6]
#[1,2,3,4] n [3,4,5,6] = [3,4] 

