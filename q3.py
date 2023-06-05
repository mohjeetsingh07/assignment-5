a = float(input("Enter Side 1: "))
b = float(input("Enter Side 2: "))
c = float(input("Enter Side 3: "))

s = float((a+b+c)/2)

if a + b > c and c + b > a and a + c > b:
    print("Yes, the combination of sides is possible and the Area of Triangle = ", (s*(s-a)*(s-b)*(s-c))**0.5)
else:
    print("Combination of side is not possible")