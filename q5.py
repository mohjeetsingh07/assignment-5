rows = int(input("Enter Rows: "))

alphabet = 65

for i in range(0, rows):
    for j in range(0, i+1):
        ch = chr(alphabet)
        print(ch, end=" ")
        alphabet +=1
        if alphabet > 90:
            alphabet = 65
    print()