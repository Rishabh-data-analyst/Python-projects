# Write a python code to print all distinct element of a list.
"""lsit1 = [11,33,34,11,56,85,33,67,34,85]
print(set(list1))"""


# Create two sets from a given set of numbers to separate even and odd numbers.
"""num = {12,33,45,42,67,39,37,23,62}
oddset = set()
evenset = set()
for i in num:
    if i%2 == 1:
        oddset.add(i)
    else:
        evenset.add(i)
print(oddset, evenset)"""

# Create a dict object where N natural numbers are keys and their squares are data values.
"""dictonary = {n:n**2 for n in range(1, int(input("Enter a number"))+1)}
print(dictonary)"""

# Sort a dictonary by its keys in descending order.
"""dictonary = {n:n**2 for n in range(1, int(input("Enter a number"))+1)}
lis = sorted(dictonary, reverse=True)
for k in lis:
    print(k,' ',dictonary[k])"""
