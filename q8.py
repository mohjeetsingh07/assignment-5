list = []
list1 = []
list2 = []
list3 = []
list4 = []
count = {}

for i in range(10):
    x = list.append(int(input(f"Enter Number {i+1}: ")))

for num in list:
    if num > 0:
        list1.append(num)
    
    elif num < 0:
        list2.append(num)

    if num%2 == 1:
        list3.append(num)

    if num%4 == 0:
        list4.append(num)

for num in list:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print("Postive Numbers are: ", list1)
print("Negative Numbers are: ", list2)
print("Odd Numbers are: ", list3)
print("Even Numbers are: ", list4)
print(count)