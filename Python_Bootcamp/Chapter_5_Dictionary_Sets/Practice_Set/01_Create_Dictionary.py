# 01 Write a program to create a dictionary of Hindi words with values as their English translation. Provide the user with an option to look it up!

def createDic(key, val, sampleDict):
    sampleDict.update({key: val})
    print(sampleDict)


if __name__ == '__main__':
    toss = 1
    sampleDict={}

    while toss == 1:
        hin, eng = input("Enter hindi work and its english meaning = ").split()
        createDic(hin, eng,sampleDict)
        dec = input("Would you like to make another entry? y or n ")
        if not (dec.lower() == 'y'):
            toss = 0

    choice = input("Would you like to select the value from the list? " + str(sampleDict.keys()) + " = ")
    print("English translation = ", sampleDict.get(choice))
