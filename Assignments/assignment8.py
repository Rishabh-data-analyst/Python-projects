#Write a python code to print each character of a string with its corresponding unicode.
'''x = input("Enter your name")
for i in x:            # where i is itreable
    print(i, ord(i))'''

#Write a python code to print only vowels of the given string.
'''x = input("Enter a string")
for i in x:
    if i in "aeiouAEIOU":
        print(i)'''

#Write a python code to count occurrence of spaces in a given string.
'''x = input("Enter a string")
count = 0
for i in x:
    if i == " ":
        count += 1
        print("count =",count)'''

#Write a python code to print unique digits of a given integer.
'''x = input("Enter an integer")
count = 0
unique = set(x)
for i in unique:
    count += 1
    print("the unique digits are", count)'''

#Write a python code to count number of digits in a given number.
'''num = input("Enter numbers")
count = 0
for i in num:
    count += 1
    print("number of digits are", count)'''

#Write a python code to print the first 10 multiples of 5.
'''for i in range (1,11):
    print(5*i, end= " ")'''

#Write a python code to print first 10 multiples of N.
'''num = int(input("Enter a number"))
for i in range (1,11):
    print(i*num, end= " ")'''

#Write a python code to print first M multiples of N.
'''num = int(input("Enter the number of table"))
multi = int(input("Enter the number at which you want the table"))
for i in range(1,multi+1):
    print(num*i, end= " ")'''


