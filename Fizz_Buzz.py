# Fizz Buzz program
for num in range(1, 61):
    # Check if the number is divisible by both 3 and 5 first
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # Check if the number is divisible by 3
    elif num % 3 == 0:
        print("Fizz")
    # Check if the number is divisible b
    elif num % 5 == 0:
        print("Buzz")
    # If none of the above conditions are met, print the number itself
    else:
        print(num)