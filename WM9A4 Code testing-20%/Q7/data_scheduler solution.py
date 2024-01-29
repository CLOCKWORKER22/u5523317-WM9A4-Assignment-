
from datetime import datetime

def date_passed(todays_date, scheduled_date):
    # Define the format for the date strings
    date_format = "%d %B"

    # Function to convert date strings to datetime objects
    def convert_to_datetime(date_str):
        day_str, month_str = date_str.split()
        day = int(day_str[:-2])  # Extract day and convert to integer
        month = datetime.strptime(month_str, "%B").month  # Convert month name to month number
        return datetime(datetime.now().year, month, day)

    # Convert date strings to datetime objects
    today_datetime = convert_to_datetime(todays_date)
    scheduled_datetime = convert_to_datetime(scheduled_date)

    # Compare dates and print the appropriate message
    if today_datetime == scheduled_datetime:
        print("The scheduled date is today.")
    elif today_datetime > scheduled_datetime:
        print("The scheduled date has passed.")
    else:
        print("The scheduled date is yet to pass.")

# Example usage
todays_date = input("Please enter today's date: ")
scheduled_date = input("Please enter the scheduled date: ")

result = date_passed(todays_date, scheduled_date)
print(result)
