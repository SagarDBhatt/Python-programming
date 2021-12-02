def detectDbSpace(string):
    cnt = string.count("  ")
    print("Count = ", cnt)


if __name__ == '__main__':
    string = input("Enter the string = ")
    detectDbSpace(string)
