# Write a program that finds out whether a given name is present in a list or not.

init_list = []

while True:
    init_list.append(input("Enter names = \t"))
    if (input("Would you like to continue = \t").lower()) == 'n':
        break

if init_list.count(input("Enter Matching name = \t")) == 0:
    print("No match")

else:
    print("Matched")