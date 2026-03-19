#Write a python code to print first N even natural numbers.
'''num = eval(input("Enter a number"))
for i in range(1,num+1):           #where i is iterable
    print(i**2, end= " ")'''

#Write a python code to print first odd natural numbers.
'''num = int(input("Enter a number"))
for i in range(1,num+1):
    print(2*i-1, end= " ")'''

#Write a python code to print squares of first N natural numbers.
'''num = int(input("Enter a number"))
for i in range(1,num+1):
    print(i**2, end= " ")'''

#Write a python code to print cubes of first N natural numbers.
'''num = int(input("Enter a number"))
for i in range(1,num+1):
    print(i**3, end=" ")'''

#Write a python code to display all prime numbers within a range. start range =15 and end range = 45
'''start = int(input("Enter starting number of the range"))
end = int(input("Enter ending number of the range"))
for i in range(start, end):
    for x in range(2,i):
        if i % x ==0:
            break
    else:
        print(i, end= " ")'''

#Write a python code to calculate sum of first N natural numbers.
'''num = int(input("Enter a number"))
sum = 0
for i in range(1,num+1):
    sum += i
print("the sum of the number is ", sum)'''

#Write a python code to calculate sum of squares of first N natural numbers.
'''num = int(input("Enter a number"))
sum = 0
for i in range(1,num+1):
    sum += i**2
print("the sum of the square of the number is", sum)'''

#Write a python code to calculate sum of cubes of first N natural numbers.
'''num = int(input("Enter a number"))
sum = 0 
for i in range(1, num+1):
    sum += i**3
print("The sum of the number is ", sum)'''

#Write a python code to calculate sum of first N odd natural numbers.
'''num = int(input("Enter a number"))
sum = 0
for i in range(1, num+1):
    sum += 2*i-1
print("the sum of the odd number is ", sum)'''

#Write a python code to calculate num of first N even natural numbers.
'''num = int(input("Enter a number"))
sum = 0
for i in range(1, num+1):
    sum += 2*i
print("the sum of the even number is ", sum)'''