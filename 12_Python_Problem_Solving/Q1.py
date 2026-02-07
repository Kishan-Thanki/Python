# Question: 1
# Movie Ticket Pricing

def age() -> None:
    age = int(input("Enter your age: "))

    if age < 13:
        print("User is Child")
    elif age < 20:
        print("User is Teenager")
    elif age < 60:
        print("User is Adult")
    else:
        print("User is Senior Citizen")

def app() -> None:

    age()

if __name__ == "__main__":
    app()