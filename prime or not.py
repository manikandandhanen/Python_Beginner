# Find Prime Number or not
num = int(input("Enter the value: "))
flag = True
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = False
            break
if flag:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

