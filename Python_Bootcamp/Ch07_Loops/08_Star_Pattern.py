# *
#
# **
#
# *** for n = 3

n = int(input("Enter number -- "))

for i in range(1, 2*n):
    for j in range(1,i+1):
        if j%2 != 0 and i%2!=0:
            print("*",end="")
    print()

