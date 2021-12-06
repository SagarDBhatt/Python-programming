# Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use keys as their names. Assume that the names are unique.

friends = ['Sam', "Ram", 'Bam', 'Jam']
dict_Friends = {}

for i in friends:
    print(i)
    # languges.append(input("Enter your favourite language" + i + " = "))
    a = input("Enter your favourite language, " + i + " = ")
    dict_Friends[i] = a

print(dict_Friends)

