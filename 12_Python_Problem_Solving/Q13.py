# Question: 13
# Multiplication Table Printer

def multiplication_table_printer(n) -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        print(f"{n} * {i} = {n * i}")

def app() -> None:
    n = int(input("Enter N: "))
    multiplication_table_printer(n)

if __name__ == "__main__":
    app()