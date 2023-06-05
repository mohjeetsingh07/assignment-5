r = int(input("Enter upper limit: "))
for a in range(2, r+1):
    if all(a % i for i in range(2, a)):
        print(a)