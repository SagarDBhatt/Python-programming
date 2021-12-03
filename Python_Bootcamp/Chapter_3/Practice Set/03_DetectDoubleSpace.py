# Ex - 3 : Write a program to detect double spaces in a string.

def detectDbSpace(string):
    cnt = string.count("  ")
    print("Count = ", cnt)


# Ex - 4 :: Replace the double spaces from problem 3 with single spaces.

def replaceDbSpace(string):
    str2 = string.replace("  "," ")
    print(str2)


if __name__ == '__main__':
    string = input("Enter the string = ")
    detectDbSpace(string)
    replaceDbSpace(string)


