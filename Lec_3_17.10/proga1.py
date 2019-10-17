age = 5

if age > 10:
    print("OK")
elif age >6 and age < 9:
    print("SO SO")
else:
    print("NOT OK!")


num = 1
den = 0

try:
    print(num/den)
except:
    print("ZERO DIVISION")