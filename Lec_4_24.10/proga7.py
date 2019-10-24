# КОРТЕЖИ -- tuple()
a = tuple()

my_tup = ()
print(type(my_tup))
my_tup2 = (1,2,3,4,56,78)
print(my_tup2)

empty = (1,)
print(empty)

new_tup = empty + my_tup2
print(new_tup)

print(dir(new_tup))
new_tup[-1] = 20
