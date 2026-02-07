# Question: 18
# Prime Number Checker

def is_prime(n) -> bool:
    if n < 1:
        return True
    
    for i in range(2, int(n / 2) + 1):
        if (n % i) == 0:
            return False
    
    return True

def app() -> None:
    n = int(input("Enter N: "))
    print("Prime Number Checker: ", is_prime(n))

if __name__ == "__main__":
    app()