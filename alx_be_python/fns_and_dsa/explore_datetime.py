from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print("\n Current date and time:", formatted_date)

def calculate_future_date(days_to_add):
    current_date = datetime.now()  # Get today's date
    future_date = current_date + timedelta(days=days_to_add)  # Add days
    formatted_future = future_date.strftime("%Y-%m-%d")

    print("Future date after", days_to_add, "days will be:", formatted_future)

def main():
    print("Welcome to the Date Explorer!\n")
    display_current_datetime()

    user_input = input("\nHow many days would you like to add to today's date? ")

    if user_input.isdigit():
        days = int(user_input)
        calculate_future_date(days)
    else:
        print("Oops! That wasn't a valid number. Please enter a whole number like 5 or 10.")

if __name__ == "__main__":
    main()
