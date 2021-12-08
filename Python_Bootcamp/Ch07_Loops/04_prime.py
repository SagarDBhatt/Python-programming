# Write a program to find whether a given number is prime or not.

flag = True

while flag:
    try:
        num = int(input("Enter number: "))
        flag = False

    except Exception:
        print('Invalid number!!')
        pass

flag_np = False
for i in range(2, num):
    if num % i == 0:
        flag_np = True

if flag_np:
    print("Not a prime number")
else:
    print("Prime number")
