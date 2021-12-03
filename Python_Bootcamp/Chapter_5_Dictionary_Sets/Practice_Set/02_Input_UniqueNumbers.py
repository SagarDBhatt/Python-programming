# Write a program to input eight numbers from the user and display all the unique numbers (once).

initSet = set()

for i in range(0, 8):
    num = input("enter number == ")
    initSet.add(num)

print(initSet)
