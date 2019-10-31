n = 0
total_set = set()
while n < 2:
    print("Enter students on lesson #", n+1)
    names = set()
    while True:
        name = input("Enter name or EXIT: ")
        if name == 'EXIT':
            break
        else:
            names.add(name)
    if n == 0:
        total_set = total_set.union(names)
    else:
        total_set = total_set.union(names)

    n += 1

print("Unique students for IN LESS 1 LESSON: ", total_set)