def is_leap_year(year):
    # Leap year logic
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Test the function
year_to_check = int(input("Enter a year to check for leap year: "))
result = is_leap_year(year_to_check)

if result:
    print("True") 
else:
    print("False")

# if result: print(f"{year_to_check} is a leap year.") else: print(f"{year_to_check} is not a leap year.")

text = input("Please enter year")
number = int(text)
result = is_leap_year(number)
print(result)