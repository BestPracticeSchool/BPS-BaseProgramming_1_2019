names = set(['Kyle', 'Sarah', 'Tomas', 'Eric', 'Ira', 'Anna', 'Bob', 'Mark', 'Alice'])
print(names.__sizeof__())
names = list(names)
print(names.__sizeof__())
names.sort()
names.append("?")
names = set(names)
for name in names:
    print(name)