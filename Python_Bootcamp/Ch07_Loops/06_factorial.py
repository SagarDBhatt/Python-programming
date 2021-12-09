# Write a program to calculate the factorial of a given number using for loop.

def findFactorial(n):
    factorial = 1

    for i in range(1,n+1):
        factorial *= i

    return factorial


if __name__ == '__main__':
    num = int(input("Enter N = "))
    result = findFactorial(num)
    print("Factorial of ", num, " is = ", result)