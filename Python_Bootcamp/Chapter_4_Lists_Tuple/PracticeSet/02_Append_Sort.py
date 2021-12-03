# 02_ Write a program to accept the marks of 6 students and display them in a sorted manner.

def sortedMarks(lst):
    lst.sort()
    print(lst)


if __name__ == '__main__':
    ls = []

    # for x in range(0, 6):
    while len(ls) <= 5:
        try:
            val = input("Enter number = ")
            val = int(val)

        except:
            continue

        ls.append(val)

    sortedMarks(ls)
