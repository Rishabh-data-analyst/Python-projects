#Write a python code to calculate factorial of a given number.
'''num = int(input("Enter a number"))
facto = 1
for i in range(1,num+1):
    facto = facto*i
print("factorial of the given number is ", facto)'''

#Write a python code to count digits in a given number.
'''num = int(input("Enter a number"))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("the number of digits in the numbers are ", count)'''

#Write a python code to calculate sum of digits of a given number.
'''num = int(input("Enter a number"))
sum = 0
while num > 0:
    sum = sum + num % 10
    num = num // 10
print("the sum of the digits of the number is", sum)'''

#Write a python code to calculate sum of elements of a list.
'''lst = [int(i) for i in input("Enter numbers separated by comma"). split(",")]
sum = sum(lst)
print(sum)'''

#Write a python code to calculate average of elements of a list.
'''lst = [int(i) for i in input("Enter  numbers separated by comma").split(",")]
avg = sum(lst)/len(lst)
print(avg)'''

#Write a python code to create a list of squares of numbers of a given list.
'''num = [int(i) for i in input("Enter numbers seperated by comma").split(",")]
square = [i**2 for i in num]
print(square)'''

#Write a python code to sort list in descending order.
'''lst = [ 1,3,4,5,6,9,33,59]
lst.sort(reverse = True)
print(lst)'''

#Write a python code to create a list from a given list by selecting only even places elements.
'''lst = [int(i) for i in input("Enter numbers seperated by comma").split(",")]
e = 1
new_list = []
for i in lst:
    if e %2 == 0:
        new_list.append(i)
        i += 1'''