# -----------------------------------------------------------
# 🫖 Python Strings
# -----------------------------------------------------------

# A string is basically something written within quotes.
# It can be inside single quotes '', double quotes "" or even triple quotes """ """.
Tea = "Lemon Tea"

# You can print it directly
print(Tea)


# -----------------------------------------------------------
# 🧩 String as Sequence (Indexing)
# -----------------------------------------------------------
# Now remember — a string in Python behaves like a list.
# So, each character has a position (index), starting from 0.
# Let's say you want the first character of TEA — how would we get it?

first_char = Tea[0]
print(first_char)

# Since it's 0-indexed, Tea[0] gives us the first letter, Tea[1] gives the second, and so on.


# -----------------------------------------------------------
# 🍋 String Slicing (Dicing)
# -----------------------------------------------------------
# Suppose we want to extract a portion of the string.
# We can do that using slicing: string[start:end]
# Remember: 'end' is excluded!

slice_tea = Tea[:5]
print(slice_tea)  # Output: Lemon


# -----------------------------------------------------------
# 🔢 More Slicing Examples
# -----------------------------------------------------------
number_list = "0123456789"

print(number_list[:])       # everything
print(number_list[3:])      # from index 3 to end
print(number_list[:7])      # from start till 6
print(number_list[3:7])     # from index 3 till 6
print(number_list[0:7])     # from 0 till 6
print(number_list[0:7:2])   # third parameter is step (hopping)


# -----------------------------------------------------------
# ☕ String Methods
# -----------------------------------------------------------
# Strings are usually Unicode, and they come with tons of helpful methods.
chai = "Masala Chai"

print(chai.lower())               # converts to lowercase
print(chai.upper())               # converts to uppercase
print(chai.strip())               # removes extra spaces from both sides
print(chai.replace("Masala", "Lemon"))  # replace words


# -----------------------------------------------------------
# 🍵 Split & Join
# -----------------------------------------------------------
# Sometimes, a single string might contain a list-like structure, like this:
Tea = "Lemon, Ginger, Masala, Green"

# If you want to convert this into a list, you can use split()
print(Tea.split(", "))

# And to go the other way — list back into string — use join()
tea_variety = ["Masala", "Lemon", "Ginger"]
tea_variety_string = ", ".join(tea_variety)
print(tea_variety_string)


# -----------------------------------------------------------
# 🔍 Searching & Counting
# -----------------------------------------------------------
# You can search inside a string using find()
print(Tea.find("emon"))   # returns starting index if found
print(Tea.find("Emon"))   # if not found, returns -1

# To count how many times something appears in a string
print(Tea.count("G"))


# -----------------------------------------------------------
# 🧾 String Formatting
# -----------------------------------------------------------
# Let’s say you want to print values inside a sentence dynamically.
Tea = "Masala"
quantity = 2

order = "I ordered {} cups of {} tea".format(quantity, Tea)
print(order)

# Or using f-strings (modern and cleaner)
order = f"I ordered {quantity} cups of {Tea} tea"
print(order)


# -----------------------------------------------------------
# 📏 Length of String
# -----------------------------------------------------------
print(len(tea_variety_string))


# -----------------------------------------------------------
# 🔁 Looping Through String
# -----------------------------------------------------------
# Sometimes you may want to print each character one by one
for i in Tea:
    print(i, end=' ')
print('\n')


# -----------------------------------------------------------
# 🧠 Quotes, Escape Characters & Raw Strings
# -----------------------------------------------------------
# Sometimes you need to include quotes *inside* a string
Tea = "He said, \"Masala Chai\" is Awesome"
print(Tea)

# Example: newline (\n)
Tea = "Masala\nChai"
print(Tea)  # prints in two lines

# If you don’t want Python to treat \n as a newline, use a raw string
Tea = r"Masala\nChai"
print(Tea)

# Same for file paths (Windows-style)
path = r"c:\user\pwd"
print(path)


# -----------------------------------------------------------
# ❓ Membership Test in Strings
# -----------------------------------------------------------
Tea = "Masala Chai"
print("Masala" in Tea)   # True
print("Green" in Tea)    # False
