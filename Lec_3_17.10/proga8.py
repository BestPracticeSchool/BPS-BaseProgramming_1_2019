
# WHILE LOOP - ЦИКЛ С ПРЕДУСЛОВИЕМ
# FOR LOOP - RANGE BASED FOR LOOP - цикл, основанный на ДИАПАЗОНАХ

i = 1
while i < 200:
    print(i)
    i = i + 1


print("ALLES")

for i in range(0,1000,2):
    print(i)

# range(start, stop, step = 1)

for j in range(1,200):
    print(j)
    if j == 185:
        break
    if j == 181:
        continue
        #print("HERE CONTINUE")

print("ALLES")