# Question: 8
# Password Strength Checker

def check_pass() -> None:
    password = input("Check your password: ")

    if len(password) < 6:
        print("Weak")
    elif len(password) < 11:
        print("Medium")
    else:
        print("Strong")


def app() -> None:
    check_pass()

if __name__ == "__main__":
    app()