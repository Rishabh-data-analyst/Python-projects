import re
import math
from functools import reduce

# ---------- Helper Functions ----------

def extract_numbers(text):
    return list(map(int, re.findall(r'-?\d+', text)))

def calculate_lcm(numbers):
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)
    return reduce(lcm, numbers)

def calculate_hcf(numbers):
    return reduce(math.gcd, numbers)

# ---------- Core Function ----------

def smart_calculator(user_input):
    text = user_input.lower()

    try:
        numbers = extract_numbers(text)

        # Addition
        if "add" in text or "sum" in text or "plus" in text:
            return sum(numbers)

        # Subtraction
        elif "subtract" in text:
            if len(numbers) >= 2:
                return numbers[1] - numbers[0]   # "subtract 10 from 25"
            return "Need at least 2 numbers"

        elif "minus" in text:
            return numbers[0] - numbers[1]

        # Multiplication
        elif "multiply" in text or "multiplied" in text or "times" in text:
            result = 1
            for num in numbers:
                result *= num
            return result

        # Division
        elif "divide" in text or "divided" in text:
            return numbers[0] / numbers[1]

        # Power
        elif "power" in text or "raised to" in text:
            return numbers[0] ** numbers[1]

        # Square Root
        elif "square root" in text:
            return math.sqrt(numbers[0])

        # Factorial
        elif "factorial" in text:
            return math.factorial(numbers[0])

        # LCM
        elif "lcm" in text:
            return calculate_lcm(numbers)

        # HCF / GCD
        elif "hcf" in text or "gcd" in text:
            return calculate_hcf(numbers)

        else:
            return "Sorry, I couldn't understand the operation."

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"Error: {str(e)}"

# ---------- Main Program ----------

def main():
    print("🧮 Smart Calculator (Type 'exit' to quit)\n")

    while True:
        user_input = input("Enter your query: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        result = smart_calculator(user_input)
        print("Result:", result)
        print()

# Run program
if __name__ == "__main__":
    main()