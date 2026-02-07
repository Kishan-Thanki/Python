# Question: 3
# Grade Calculator

def grade_calculate() -> None:
    score = int(input("Enter your grade: "))

    if score > 100:
        exit()
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"Your Grade Is: {grade}")

def app() -> None:
    grade_calculate()

if __name__ == "__main__":
    app()