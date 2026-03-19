# Write a python code to create a list of first N natural numbers.
"""num = int(input("Enter the number"))
list = []
for i in range(1, num+1):
    list.append(i)
print("The list is", list)"""

# Write a python code to create a list of first N terms of Fibonacci series.
"""num = int(input("Enter a num to get fibonacci series"))
a,b = 0,1
fibo = []
for i in range(num):
    fibo.append(a)
    a,b = b, a+b
print("The fibonacci seires is", fibo)"""

# Write a python code to create a list of first N prime numbers.
"""num = int(input("Enter a number to get prime numbers"))
list = []
for i in range(1,num+1):
    for x in range(2,i):
        if i%x ==0:
            break
    else:
        list.append(i)
print("The list of prime numbers is", list)"""

"""Write a python code to create two lists from a given list of numbers in such a way that the first list 
can have only positive numbers and second list can have only non positive numbers"""
"""original_list=[2,3,4,5,6,-9,-8,-7,-6,-5]
plist = []
nplist = []
for i in (original_list):
    if i > 0:
        plist.append(i)
    else:
        nplist.append(i)
print("The positive list is", plist)
print("The non positive list is", nplist)"""