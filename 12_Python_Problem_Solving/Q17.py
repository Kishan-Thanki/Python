# Question: 17
# Validate Input

def validate_input(n) -> bool:
    if n in range(2, 10):
        return True

    return False

def app() -> None:
    
    while True:
        n = int(input("Enter N in range 1 to 10: "))
        if validate_input(n):
            break

if __name__ == "__main__":
    app()