# Question: 12
# Counting Positive Numbers

def even_num_sum(n) -> int:
    sum = 0
    for i in range(1, n + 1):
        if (i % 2) == 0:
            sum = sum + i
    return sum

def app() -> None:
    n = int(input("Enter N: "))

    print("Sum Of Even Number:",even_num_sum(n))

if __name__ == "__main__":
    app()