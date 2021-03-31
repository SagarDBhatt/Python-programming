testCases = int(input())

for i in range(testCases):

    try:
        a, b = map(int, input().split())
        print(a // b)
    # print(testCases, a, b)

    except Exception as e:
        print("Error Code:", e)