# Write a program to find the greatest of four numbers entered by the user.
inp_list = []
for i in range(0, 4):
    inp_list.append(int(input("Enter the number = ")))
    print(inp_list)

f_Val = inp_list[0]
for i in inp_list:
    if i > f_Val:
        f_Val = i

print("Maximum value = ", f_Val)
