# Question: 16
# Factorial Calculator

def factorial(n) -> int:
    fact = 1
    while n > 0:
        fact = fact * n
        n -= 1
    
    return fact

def app() -> None:
    n = int(input("Enter N: "))
    print("Factorial Calculator:",factorial(n))

if __name__ == "__main__":
    app()