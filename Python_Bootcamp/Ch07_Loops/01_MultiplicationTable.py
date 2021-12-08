# Write a program to print the multiplication table of a given number using for loop.

num = int(input("Enter table number = \n"))

for i in range(1, 11):
    print(num, " * ", i, " = ", num * i)

## Same problem with while loop.

i = 1
inp = int(input("Enter number = \n"))
while i <= 10:
    print(inp, " * ", i, " = ", inp * i)
    i += 1
