'''
Check the type of the variable assigned using the input() function.
'''

a = input("Enter value 1 = ")

try:
    try:
        a = int(a)
        print("Type of value 1 = ", type(a))

    except:
        try:
            a = float(a)
            print("Type of value 1 = ", type(a))

        except:
            raise TypeError

except:
    a = str(a)
    print("Type of value 1 = ", type(a))

