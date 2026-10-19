import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("Not a quadratic equation")
else:
    d = b**2 - 4*a*c
    if d > 0:
        print("Real & distinct roots:", (-b + math.sqrt(d)) / (2*a), (-b - math.sqrt(d)) / (2*a))
    elif d == 0:
        print("Real & equal roots:", -b / (2*a))
    else:
        print("Complex roots:", complex(-b, math.sqrt(-d)) / (2*a), complex(-b, -math.sqrt(-d)) / (2*a))
