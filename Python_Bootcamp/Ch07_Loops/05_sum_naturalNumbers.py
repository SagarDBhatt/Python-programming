# Write a program to find the sum of first n natural numbers using a while loop.

def findSum(num):
    sumNum = 0

    while num > 0:
        sumNum += num
        num -= 1

    return sumNum


if __name__ == '__main__':
    number = int(input("Enter the number =  "))
    print("Sum of first ", number, " numbers = ", findSum(number))
