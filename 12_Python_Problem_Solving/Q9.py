# Question: 9
# Leap Year Checker

def check_leap_year() -> None:
    try:
        year = int(input("Enter a year: "))

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year. ✅")
        else:
            print(f"{year} is not a leap year. ❌")
            
    except ValueError:
        print("Invalid input. Please enter a whole number (e.g., 2024).")

def app() -> None:
    check_leap_year()

if __name__ == "__main__":
    app()