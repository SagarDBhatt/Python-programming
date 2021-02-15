# Problem Statement

# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
#
#
# Given a full name, your task is to capitalize the name appropriately.
#
# Input Format
#
# A single line of input containing the full name, .
#
# Constraints
#
# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
#
# Output Format
#
# Print the capitalized string, .
#
# Sample Input
#
# chris alan
# Sample Output
#
# Chris Alan

s = input("Enter Text: ")
# for i in range(0, len(s)):
#     space_index = s.find(" ")
#     temp = s.replace(s[space_index + 1], s[space_index + 1].upper())
#     print(temp.replace(temp[0], temp[0].upper()))

temp = s.split()
for val in temp:
    s = s.replace(val, val.capitalize())
    #print(val.replace(val[0], val[0].upper()))
print(s)