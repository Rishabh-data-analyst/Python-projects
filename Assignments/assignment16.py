# Write a python function to print first N odd natural numbers.
"""def odd(n):
    for i in range(1,n+1):
        print(2*i-1, end= " ")
odd(5)"""

# Write a python function to print first N prime numbers.
"""def prime(n):
    for i in range(1,n+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i, end= " ")
prime(23)"""

# Write a python function to  print all prime numbers between two given numbers.
"""def prime(start,end):
    for i in range(start,end+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i, end= " ")
prime(13,73)"""

# Write a python function to print First N terms of Fibobacci series.
"""def fibo(n):
    a,b = 0,1
    for i in range(1,n+1):
        print(a,end= " ")
        a,b = b,a+b
fibo(8)"""

# Write a python function to print all factors of a given number.
"""def factor(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end= " ")
factor(16)"""

# Write a python function to calculate LCM of two numbers.
"""def lcm(a,b):
    l  = a if a > b else b
    while l <= a*b:
        if l % a == 0 and l % b == 0:
            break
        l += 1
    return("lcm of the number is", l)
print(lcm(8,16))"""

# Write a python function to count words in a string.
"""def count(words):
    return len(words.split(" "))
print(count("i am what i am i do whatever i like to do."))"""

# Write a python function to create a list of Prime numbers between two given numbers.
"""def prime(a,b):
    lis = []
    for i in range (a,b+1):
        for j in range (2,i):
            if i % j == 0:
                break
        else:
            lis.append(i)
    return lis
print(prime(7,23))"""


# Write a python function to find all common factors of two given numbers.
"""def factors(a, b):
    lis = []
    f = a if a < b else b
    while f >= 1:
        if a % f == 0 and b % f == 0:
            lis.append(f)
        f -= 1
    return lis


print(factors(12, 18))
"""
# Write a python function to remove duplicate elements from a given list.
"""def remove(lis):
    return list(set(lis))

l = [1,2,3,4,5,2,4,2,3]
print(remove(l))"""

# Write a python function to check if two given list have same elements in any order or not.
"""def same(lis1,lis2):
    if sorted(lis1) == sorted(lis2):
        return True
    else:
        return False

l1 = [1,2,3,4,5]
l2 = [4,3,5,1,2]
print(same(l1,l2))"""

# assignment 37 se start karna hai.
