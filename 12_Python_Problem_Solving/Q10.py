# Question: 10
# Pet Food Recommendation

def recommend_pet_food() -> None:
    species = input("Enter pet species (Dog or Cat): ").strip().lower()
    
    try:
        age = float(input("Enter pet's age in years: "))
        
        if age < 0:
            print("Age cannot be negative. Please try again.")
            return

        recommendation = "Unknown"

        if species == 'dog':
            if age < 2:
                recommendation = "Puppy food"
            elif age <= 7: 
                recommendation = "Adult dog food"
            else: 
                recommendation = "Senior dog food"
        
        elif species == 'cat':
            if age < 1:
                recommendation = "Kitten food"
            elif age <= 5: 
                recommendation = "Adult cat food"
            else: 
                recommendation = "Senior cat food"
        
        else:
            print(f"Sorry, we don't have recommendations for '{species}'.")
            return

        print(f"Recommendation for a {age}-year-old {species}: {recommendation} 🐾")

    except ValueError:
        print("Invalid input. Please enter a number for the age.")

def app() -> None:
    recommend_pet_food()

if __name__ == "__main__":
    app()