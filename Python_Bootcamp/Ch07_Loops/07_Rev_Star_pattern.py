#     *
#
#   ***
#
# ***** for n=3

def draw_pattern(n):
    for i in range(2 * n - 1, 0, -1):
        for j in range(1, 2*n, 1):
            if i % 2 == 0:
                print(" ", end="")
            elif j < i:
                print(" ", end="")
            elif j >= i:
                print("*", end="")
            else:
                pass

        print()


if __name__ == '__main__':
    n = int(input("Enter N = "))
    draw_pattern(n)
