# Question: 14
# Reverse String Using Loop

def reverse_string(s) -> str:
    rstr = ""
    for char in s:
        rstr = char + rstr
    return rstr

def app() -> None:
    s = input("Enter string: ")
    print("Reversed String:",reverse_string(s))

if __name__ == "__main__":
    app()