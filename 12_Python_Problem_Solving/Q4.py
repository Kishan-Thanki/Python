# Question: 4
# Fruit Ripeness Checker

def fruit_riper() -> None:
    
    fruit = input("Enter Fruit: ")
    color = input("Enter Fruit Current Color: ")

    if color == "Green":
        ripness = "Unripe"
    elif color == "Yellow":
        ripness = "Ripe"
    elif color == "Brown":
        ripness = "Overripe"
    else:
        ripness = "Undetermined"
    
    print(f"{fruit} is {ripness}")

def app() -> None:
    fruit_riper()

if __name__ == "__main__":
    app()