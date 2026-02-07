# Question: 5
# Weather Activity Suggestion

def weather_activity_suggestioner() -> None:
    
    weather = input("Enter Current Weather: ").lower()

    if weather == "sunny":
        activity = "Go for a walk"
    elif weather == "sainy":
        activity = "Read a book"
    elif weather == "snowy":
        activity = "Build a snowman"
    else:
        activity = "Provide an valid weather"
    
    print(f"{activity}")

def app() -> None:
    weather_activity_suggestioner()

if __name__ == "__main__":
    app()