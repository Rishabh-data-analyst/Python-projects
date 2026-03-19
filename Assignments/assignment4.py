#Write a python code to print True if the string 'my' is a member in a string entered by user.
'''line = input("Enter a line of strings")
print('my' in line)'''

#Write a python code to check wheather a given number is positive or non-positive.
'''num = int(input("Enter a number"))
if num >=1:
    print("The number is positive")
else:
    print("The number is non-positive")'''

#Write a python code to check whether a given number is divided by 5 or not.
'''num = int(input("Enter a number"))
if num % 5 ==0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")'''

#Write a python code to check whether a given number is even or odd.
'''num = int(input("Enter a number"))
if num % 2 ==0:
    print("The number is even")
else:
    print("The number is odd")'''

#Write a python code to print greater between two numbers. Print number only once even if the numbers are the same.
'''num1, num2 = int(input("Enter first number")), int(input("Enter second number"))
if num1 == num2:
    print(num1 or num2)
elif num1 > num2:
    print(num1)
else:
    print(num2)'''

#Write a python code to print two given words in dictonary order.
'''word1, word2 = input("Enter first word"), input("Enter second word")
words = sorted((word1, word2), key = str.lower)
print(words)'''

#Write a python code to check whether a given number is a three digit number or not.
'''num = int(input("Enter a number"))
if 100<num<999:
    print("This is a three digit number")
else:
    print("This is not a three digit number")'''

#Write a python code to check whether a given number is positive, negative or zero.
'''num = int(input("Enter a number"))
if num >= 1:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")'''

#Write a python code to check a given year is a leap year or not.
'''year = int(input("Enter a year"))
if (year % 4 == 0 and year % 100 !=0) or (year % 400==0):
    print( year, "is a leap year")
else:
    print(year, "is not a leap year")'''

#Write a python code to print greater among three numbers. Print number only once even if the numbers are the same.
'''x = int(input("Enter first number"))
y = int(input("Enter second number"))
z = int(input("Enter third number"))
if x > y:
    print(x if x > z else z)
else:
    print(y if y > z else z)'''

