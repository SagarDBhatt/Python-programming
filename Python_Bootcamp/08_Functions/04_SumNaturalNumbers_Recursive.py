# Write a recursive function to calculate the sum of first n natural numbers.

# def calcSum(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum

def calcSum(n):
    if n == 1:
        return 1
    else:
        sum = 0
        sum = sum + n
        return sum + calcSum(n-1)


if __name__ == '__main__':
    n = int(input("Enter N == "))
    sum = calcSum(n)
    print(f"Sum = {sum}")