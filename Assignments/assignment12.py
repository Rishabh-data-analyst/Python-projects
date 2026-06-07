# Write a python code to check if a given string has only alphabets in it.
"""text = input("Enter a string")
print(text.isalpha())"""

# Write a python code to check if a given character is present in a given string or not.
"""text = input("Enter a string")
ch = input("Enter a character")
if ch in text:
    print("Character is present")
else:
    print("Character is not present")"""

# Write a python code to count vowels in a given string.
"""text = input("Enter a string")
count = 0
for i in text:
    if i in "aeiouAEIOU":
        count +=1

print("the number of vowels is:", count)"""

# Write a python code to count words in a given string.
"""text = input("Enter a string")
counts = 0
for i in text.split(" "):
    counts +=1
print("Total number of words are:", counts)"""

# Write a python code to reverse a string.
"""text = input("Enter a string")
print(text[::-1])"""

# Write a python code to extract numbers from a given text and store all the numbers in a list.
"""text = input("Enter a string")
num = []
for i in text.split(' '):
    try:
        num.append(float(i))
    except:
        pass
print("Total numbers are:", num)"""

# Write a python code to check whether it is a palindrome or not.
"""text = input("Enter a string")
print("Palindrome" if text == text[::-1] else "not a Palindrome")"""

# Write a python code to transform a given string to uppercase.
"""text = input("Enter a string")
print(text.upper())"""

# Write a python code to find maximum length word in a given text.
"""text = input("Enter a string")
words = text.split()

max_word = max(words, key=len)

print("Maximum length word is:", max_word)"""
