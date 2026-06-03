import time

# Predefined passage (you can change this if needed)
PASSAGE = """Python is a powerful and versatile programming language.
It is widely used for web development, data analysis, artificial intelligence,
and scientific computing. Practicing typing regularly improves speed and accuracy."""

def calculate_wpm(correct_chars, time_taken_seconds):
    words = correct_chars / 5
    minutes = time_taken_seconds / 60
    return words / minutes if minutes > 0 else 0

def calculate_accuracy(correct_chars, total_chars):
    return (correct_chars / total_chars) * 100 if total_chars > 0 else 0

def typing_test():
    print("\n===== Typing Test =====\n")
    print("Type the following passage:\n")
    print(PASSAGE)
    print("\nPress ENTER when you are ready to start...")
    input()

    print("\nStart typing below:\n")

    start_time = time.time()
    user_input = input()
    end_time = time.time()

    time_taken = end_time - start_time

    correct_chars = 0
    total_chars = len(PASSAGE)

    # Compare character by character
    for i in range(min(len(user_input), len(PASSAGE))):
        if user_input[i] == PASSAGE[i]:
            correct_chars += 1

    # Calculate results
    wpm = calculate_wpm(correct_chars, time_taken)
    accuracy = calculate_accuracy(correct_chars, total_chars)

    print("\n===== Results =====")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Typing Speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

# Run the program
if __name__ == "__main__":
    typing_test()