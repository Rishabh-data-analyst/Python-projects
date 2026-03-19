import random

print("OTP Generator and Varification")

otp = random.randint(1000, 9999)    #for otp generation
print("Your otp is :", otp)

user_input = int(input("Enter the four digits otp sent to your inbox"))   #ask user to enter otp

if user_input == otp:
    print("Your OTP varification is successful!")
else:
    print("Invalid OTP \n Try again!")