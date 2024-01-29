def compound_interest_calculator(P, r, n, t):
    # Check for valid inputs
    if P <= 0 or r < 0 or n <= 0 or t <= 0:
        raise ValueError("Invalid input. Please provide positive values for all parameters.")

    # Calculate compound interest using the formula
    A = P * (1 + r/n)**(n*t)

    return A

# Example usage
try:
    principal_amount = float(input("Enter the principal amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in decimal): "))
    compounding_frequency = int(input("Enter the number of times interest is compounded per year: "))
    investment_period = int(input("Enter the number of years for investment: "))

    result = compound_interest_calculator(principal_amount, annual_interest_rate, compounding_frequency, investment_period)

    print(f"The accumulated amount after {investment_period} years is: {result:.2f}")
except ValueError as e:
    print(e)
