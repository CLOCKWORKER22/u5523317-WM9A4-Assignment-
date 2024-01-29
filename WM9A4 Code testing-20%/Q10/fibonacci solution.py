def fibonacci_sequence(max_value):
    # Handle edge cases for 0 and negative inputs
    if max_value < 0:
        raise ValueError("Fibonacci sequence is not defined for negative numbers.")
    elif max_value == 0:
        return [0]

    # Initialize the Fibonacci sequence
    sequence = [0, 1]

    # Generate Fibonacci sequence using a while loop
    while sequence[-1] + sequence[-2] <= max_value:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)

    return sequence


try:
    input_max_value = int(input("Enter the maximum value for the Fibonacci sequence: "))
    result_sequence = fibonacci_sequence(input_max_value)

    print(f"The Fibonacci sequence up to {input_max_value} is: {result_sequence}")
except ValueError as e:
    print(e)
    
    

    

