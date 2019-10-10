num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))
# 0/0
try:
    print("Numeric value: ", num/den)
except:
    print("WOW ZERO DIVISION!")

print("String value ", str(num) +'/'+str(den))