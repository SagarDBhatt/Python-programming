def average(array):
    # your code goes here
    # print(array)
    setInt = set(array)
    # print(setInt)
    # print(sum(setInt), len(setInt))
    return sum(setInt) / len(setInt)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
