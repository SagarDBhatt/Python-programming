# # Problem Statement
#
# #Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string .
#
# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
#
# For better understanding, see the image below:
#
# banana.png
#
# Your task is to determine the winner of the game and their score.
#
# Input Format
#
# A single line of input containing the string .
# Note: The string  will contain only uppercase letters: .
#
# Constraints
#
#
#
# Output Format
#
# Print one line: the name of the winner and their score separated by a space.
#
# If the game is a draw, print Draw.
#
# Sample Input
#
# BANANA
# Sample Output
#
# Stuart 12
# Note :
# Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.

# =====================================================================
# =====================================================================


# Below solution is complex and DOES NOT pass the timely execution.
# Iterating two loops for a larger string creates issues.

# ipStr = input("Enter String: ")
# Score_Stuart = 0
# Score_Kevin = 0
# List_Substring = list()
#
#
# for i in range(len(ipStr)):
#     for j in range(i, len(ipStr)):
#         List_Substring.append(ipStr[i:j + 1])
#
# for sub in List_Substring:
#     if sub.startswith(("A", "E", "I", "O", "U")):
#         Score_Kevin += 1
#
#     else:
#         Score_Stuart += 1
#
#
# if Score_Kevin > Score_Stuart:
#     print("Kevin ", Score_Kevin)

# elif Score_Kevin == Score_Stuart:
#         print("Draw")
# else:
#     print("Stuart ", Score_Stuart)

# =====================================================================
#     ANOTHER APPROACH
# =====================================================================

ipStr = input("Enter String: ")
Score_Stuart = 0
Score_Kevin = 0

for sub in range(len(ipStr)):
    if ipStr[sub] in ("A", "E", "I", "O", "U"):
        Score_Kevin += len(ipStr) - sub
    else:
        Score_Stuart += len(ipStr) - sub


if Score_Kevin > Score_Stuart:
    print("Kevin ", Score_Kevin)

elif Score_Kevin == Score_Stuart:
    print("Draw")

else:
    print("Stuart ", Score_Stuart)