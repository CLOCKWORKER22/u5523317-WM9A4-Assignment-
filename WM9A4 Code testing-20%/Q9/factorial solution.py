def calculate_factorial(number):
    # Handle edge cases for 0 and negative inputs
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif number == 0:
        return 1
    
    # Initialize the factorial result
    factorial_result = 1

    # Calculate factorial using a for loop
    for i in range(1, number + 1):
        factorial_result *= i

    return factorial_result

# Example usage
try:
    input_number = int(input("Enter a non-negative integer to calculate its factorial: "))
    result = calculate_factorial(input_number)

    print(f"The factorial of {input_number} is: {result}")
except ValueError as e:
    print(e)
