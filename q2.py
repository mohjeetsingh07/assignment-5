Num = int(input("Enter Number: "))
Range = int(input("Enter Range: "))

for i in range(1, Range+1):
    if i%Num == 0:
        print(i)