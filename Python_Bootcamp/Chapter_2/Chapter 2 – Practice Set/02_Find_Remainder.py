'''
Write a Python program to find the remainder when a number is divided by Z(Integer).
'''


def findRemainder(a, b):
    rem = a % b
    print("Remainder of ", a, " and ", b, " = ", rem)


if __name__ == "__main__":
    a, b = input("Enter 2 numbers = ").split(",")
    a = int(a)
    b = int(b)
    try:
        if not (type(a) or type(b)) is int:
            raise TypeError("Numbers are NOT integers")
    except TypeError:
        print("Numbers are NOT integers!!")

    findRemainder(a, b)
