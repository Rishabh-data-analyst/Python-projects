#Write a pyton code to check whether a number is positive, negative or zero.
'''num = int(input("Enter a  number"))
match num:
    case _ if num > 0:
        print("The number is a positive number")
    case _ if num < 0:
        print("The number is a negative number")
    case _:
        print("zero")'''

'''Write a python code to take one data from user and evaluate the type of data. If the data is of int type then print monday.
If the data is of float type then print Tuesday. If the data is of complex type then print Wednesday.
If the data is of type bool then print Thusday.'''
'''data = eval(input("Enter a data"))
match data:
    case data if type(data)==int:
        print("Monday")
    case data if type(data)==float:
        print("Tuesday")
    case data if type(data)==complex:
        print("Wednesday")
    case data if type (data)==bool:
        print("Thusday")'''

#Write a python code to take a string from the user. If the string is a part of "mysirg" then print One, if the string is a part of "education" print "Two" and if the string is a part of "services" then print "Three".
'''x = input("Enter a string")
match x:
    case x if x in "mysirg":
        print("One")
    case x if x in "education":
        print("Two")
    case x if x in "services":
        print("Three")
    case _:
        print("Not my type")'''


