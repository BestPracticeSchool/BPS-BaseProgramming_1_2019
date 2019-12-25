#Класс - это инструкция по созданию объектов одного семейства.
#Атрибут/поле - это переменная, определенная внутри класса
#Метод - это функция определенная внутри класса

class Myclass:
    age = 25
    h = 193
    w = 85
    name = "Joe"


m = Myclass()
print(type(m), m)
print(m.age, m.h, m.w, m.name)

q = Myclass()
print(q)
print(q.age, q.h, q.w, q.name)

a = 20
b = 25.12
c = "Hello world"
d = True

def add():
    return 0 

kek = []

print(type(a), type(b), type(c), type(d))
print(type(add), type(kek))