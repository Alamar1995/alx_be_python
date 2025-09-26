from datetime import datetime, timedelta

def display_current_datetime():
    # Save current date and time
    current_date = datetime.now()
    # Format as YYYY-MM-DD HH:MM:SS
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted)
    return current_date

def calculate_future_date(current_date, days):
    # Calculate future date
    future_date = current_date + timedelta(days=days)
    # Format as YYYY-MM-DD
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Part 1: display current datetime
    current_date = display_current_datetime()

    # Part 2: ask user for days to add
    try:
        days = int(input("Enter the number of days to add to the current date: ").strip())
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    calculate_future_date(current_date, days)

if __name__ == "__main__":
    main()
