# Question: 7
# Coffee Customization

def coffee_customizer() -> None:
    coffee_size = input("Coffee size (e.g., Small, Medium, Large): ")
    extra_shot_input = input("Do you want an extra shot? (yes/no): ").strip().lower()

    extra_shot = ""
    if extra_shot_input in ['yes', 'y']:
        extra_shot = " with an extra shot of espresso"
    
    print(f"Order: {coffee_size} coffee{extra_shot}")

def app() -> None:
    coffee_customizer()

if __name__ == "__main__":
    app()
