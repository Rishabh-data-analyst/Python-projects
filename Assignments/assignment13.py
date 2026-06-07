#Write a python code to remove all non int values from a list.
"""data = input("Enter a list of values:")
i = 0
result = []
while i < len(data):
    if data[i].isdigit():
        result.append(int(data[i]))
    i += 1
print("List of integers:", result)"""
#Write a python code to print distinct elements along with their frequencies of occurrences in the list.
"""data = input("Enter a list of values:")
i = 0
frequency = {}
while i < len(data):
    if data[i] in frequency:
        frequency[data[i]] += 1
    else:
        frequency[data[i]] = 1
    i += 1
print("Frequencies:", frequency)"""

#Write a python code to sort a list of strings.
"""data = input("Enter a list of strings separated by space: ")
lst = data.split()
lst.sort()
print(lst)"""


#Write a python code to find first repeated string in a list of strings.
"""data = input("Enter a list of strings separated by space: ")
lst = data.split()
repeat = []
for i in lst:
    if i in repeat:
        print("First repeated string: ", i)
        break
    else:
        repeat.append(i)
else:
    print("No repeated string found")"""

#Write a python code to count strings which ends at character "s" in a list of strings.
"""data = input("Enter a list of strings separated by space: ")
lst = data.split()
count = 0
for i in (lst):
    if i.endswith('s'):
        count += 1
print("count:", count)"""

#Write a python code to create a tuple from a given list.
"""data = input("Enter a list of strings separated by space: ")
lst = data.split()
print(tuple(lst))"""

#Write a python code to reverse a tuple.
"""data = input("Enter elements separated by comma:")
tup = tuple(data.split(","))
print("Reversed tuple is: ", tup[::-1])"""

#Write a python code to create a list of tuples, where each tuple is a pair of elements, first element is uppercase character and second element is its unicode.
"""data = input("Enter elements separated by comma:")
lst = data.split()
pair = []
for i in lst:
    upper_i = i.upper()
    unicodevalue = ord(upper_i)
    pair.append((upper_i, unicodevalue))
print("List of tuples is", pair)"""

