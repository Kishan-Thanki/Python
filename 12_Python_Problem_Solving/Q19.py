# Question: 19
# List Uniqueness Checker

def is_unique(items) -> bool:
    unique_set = set()
    for item in items:
        if item in unique_set:
            print(f"Duplicate Item: {item}")
            return False
        unique_set.add(item)
    
    return True

def app() -> None:
    items = ["apple", "banana", "orange", "apple", "mango"]
    # items = ["apple", "banana", "orange", "kiwi", "mango"]
    print("Uniqueness:",is_unique(items))

if __name__ == "__main__":
    app()