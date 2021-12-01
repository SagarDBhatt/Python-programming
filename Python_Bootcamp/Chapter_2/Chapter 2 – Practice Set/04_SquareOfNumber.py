import math


def powerOfNum(a, b):
    val = math.pow(a, b)
    print("Val of ", a, " to the power of ", b, " is = ", int(val))


if __name__ == "__main__":
    a, b = input("Enter 2 numbers = ").split()
    a = int(a)
    b = int(b)
    powerOfNum(a, b)
