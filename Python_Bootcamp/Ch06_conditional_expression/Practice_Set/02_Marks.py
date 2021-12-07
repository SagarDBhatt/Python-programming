# Write a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

ls_subjects = ["s1",'s2','s3']
dict_marks = {}

for i in ls_subjects:
    try:
        dict_marks[i] = int(input("Enter marks in range of 0 to 100 for the subject of " + i + " \t"))
        if dict_marks[i] > 100 or dict_marks[i] < 0:
            raise Exception("The marks entered are outside the range 0 to 100")

    except:
        print("The marks entered are outside the range 0 to 100")
        continue

totalScore =0
for sub, marks in dict_marks.items():
    totalScore += marks

    if marks < 33:
        print("Failed")

if totalScore < 40:
    print('Failed')
else:
    print("Passed")