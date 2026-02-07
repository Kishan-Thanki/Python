# Question: 11
# Sum of Even Numbers

def count_positive_number(numbers) -> int:
    count = 0
    for i in numbers:
        if i >= 0:
            count = count + 1
    return count

def app() -> None:
    numbers = [1, -2, 3, 4, 5, 6, -7, -8, 9, 10]

    print("Positive Number Count:",count_positive_number(numbers))

if __name__ == "__main__":
    app()