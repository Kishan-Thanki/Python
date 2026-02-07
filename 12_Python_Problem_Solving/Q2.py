# Question: 2
# Movie Ticket Pricing

def m_tickets() -> None:
    day = input("Enter day: ")
    age = int(input("Enter your age: "))

    ticket_price = 12 if age >= 18 else 8

    if day == "Wednesday":
        ticket_price -= 2    

    print(f"${ticket_price}")

def app() -> None:
    m_tickets()

if __name__ == "__main__":
    app()