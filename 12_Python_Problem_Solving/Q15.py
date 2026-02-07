# Question: 15
# Find The First Non-Repeated Character

def nonrepeated_character(s) -> str:
    for char in s:
        if s.count(char) == 1:
            return char
    return ""

def app() -> None:
    s = input("Enter: ")
    print("First Non-Repeated Character:",nonrepeated_character(s))

if __name__ == "__main__":
    app()