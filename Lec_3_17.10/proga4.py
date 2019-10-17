max_h = 190
min_h = 150

# Задача. На вход программе подается рост  кандидатов в лётчики до тех пор, пока не будет введено ЛЮБОЕ ОТРИЦАТЕЛЬНОЕ ЧИСЛО.
# Определить, сколько персон из кандидатов годится в лётчики. А также минимальный и максимальный рост отобранных кандидатов.
# Если рост кандидата min_h <= рост кандидата <= max_h то он годится в лётчики.


current_max_h = -10000
current_min_h = 100000
count = 0
h = int(input("Enter H: "))
while h >= 0:
    
    if h >= min_h and h <= max_h:
        count = count + 1
        if h > current_max_h :
            current_max_h = h
        if h < current_min_h:
            current_min_h = h
    h = int(input("Enter H: "))

print("Total amount valid candidates : ", count)
print("Max H : ", current_max_h)
print("Min H: ", current_min_h)