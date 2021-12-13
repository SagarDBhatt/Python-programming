# ***
#
# **       #For n = 3
#
# *

def pattern(n):
    # for i in range(1, n + 1):
    #     for j in range(n, 0, -1):
    #         if j >= i:
    #             print("*", end="")
    #     print()
    for i in range(n):
        print("*" * (n-i))

pattern(3)
