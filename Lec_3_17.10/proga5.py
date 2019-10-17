i = 0
my_max = -1000000000
while i < 5:
    num = int(input())
    if num > my_max:
        my_max = num
        print("Current max is : ", my_max)

    i = i + 1

print("Total maximum is : ", my_max)


j = 0
my_min = 1000000000
while j < 5:
    num = int(input())
    if num  < my_min:
        my_min = num
        print("Current min is : ", my_min)

    j = j + 1

print("Total minimum is : ", my_min)


