# ================================================================
# 🔢 Python Numbers
# ================================================================
# Python’s number system is one of the most flexible among all
# programming languages — dynamic, precise, and seamlessly integrated
# with scientific computation libraries (NumPy, SciPy, etc.)
# ================================================================


# ----------------------------------------------------------------
# 💡 Key Idea:
# Compared to many languages, Python’s numeric types are *very strong*.
# In fact, after adding libraries like NumPy, Python performs at the
# same numerical level as MATLAB — which is why scientists and data
# engineers use it so much.
# ----------------------------------------------------------------

# Even Boolean values are internally treated as numbers (True = 1, False = 0)

# ----------------------------------------------------------------
# ⚙️ Numeric Categories in Python
# ----------------------------------------------------------------
# - Integers (int)
# - Floating-point numbers (float)
# - Complex numbers (complex)
# - Boolean (bool)
# - Fractions (Fraction)
# - Decimals (Decimal)
# ----------------------------------------------------------------

x = 2
y = 3
z = 4

# Basic arithmetic operations
print(x + y)   # 5
print(x - y)   # -1
print(x * y)   # 6
print(x / y)   # 0.666... (float division)
print(x // y)  # 0        (floor division)
print(x ** y)  # 8        (power)
print(x % y)   # 2        (modulus)
print((x + y) * z)  # 20


# ----------------------------------------------------------------
# 🧮 Type Promotion & Precision
# ----------------------------------------------------------------
# Python automatically promotes smaller (lower precision) types to
# higher ones when performing mixed operations.
print(40 + 2.23)  # 42.23

# But in codebases, it’s recommended to keep operands of same type.
print(float(40)), print(int(2.23))  # explicit conversions


# ----------------------------------------------------------------
# ⚡ Operator Overloading
# ----------------------------------------------------------------
# Operators like + are overloaded to work for multiple data types.
print("Hello" + " Python")  # String concatenation

# ----------------------------------------------------------------
# 🧠 Big Integers
# ----------------------------------------------------------------
# Python supports arbitrarily large integers natively.
print(2 ** 1000)  # Many languages fail here due to overflow.


# ----------------------------------------------------------------
# 🎯 Rounding & String Representations
# ----------------------------------------------------------------
result = 1 / 3.0
print(result)       # 0.3333333333333333
print(round(result, 4))  # 0.3333

# str() gives user-friendly form, repr() gives precise developer form
print(str(result))
print(repr(result))


# ----------------------------------------------------------------
# ✅ Comparisons & Boolean-Numeric Relationship
# ----------------------------------------------------------------
print(1 < 2)      # True
print(True == 1)  # True
print(False == 0) # True
print(True is 1)  # False  (different identity)
print(True + 4)   # 5 — because True behaves like 1

# Note: Using "is" with numbers gives a SyntaxWarning since it checks identity.


# ----------------------------------------------------------------
# 📚 Numeric Libraries
# ----------------------------------------------------------------
import math
import random
from decimal import Decimal
from fractions import Fraction

# Math operations
print(math.sqrt(16))
print(random.randint(1, 5))

# Numeric base conversions
print(oct(8))  # '0o10'
print(hex(255))  # '0xff'
print(bin(7))  # '0b111'

# Fractions and Decimals
print(Fraction(1, 3))
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))  # Exact 0.0


# ----------------------------------------------------------------
# ⚠️ Floating Point Precision Issue
# ----------------------------------------------------------------
print(0.1 + 0.1 + 0.1)          # 0.30000000000000004
print((0.1 + 0.1 + 0.1) - 0.3)  # 5.551115123125783e-17

# Due to binary floating-point representation.
# Use Decimal or Fraction for financial or exact arithmetic.
print(Decimal('0.1') * 3 - Decimal('0.3'))  # 0.0
print(Fraction(1, 10) * 3 - Fraction(3, 10))  # 0


# ----------------------------------------------------------------
# 🧮 Sets as Mathematical Collections
# ----------------------------------------------------------------
set_one = {1, 2, 3, 4}
print(set_one & {1, 3})       # Intersection → {1, 3}
print(set_one | {1, 3})       # Union → {1, 2, 3, 4}
print(set_one | {1, 3, 7})    # Union with new elements → {1, 2, 3, 4, 7}
print(set_one - {1, 2, 3, 4}) # Difference → set()
print(type({}))               # dict, note set — {} makes dict, use set() for empty set.


# ----------------------------------------------------------------
# 🔢 Boolean as Numeric
# ----------------------------------------------------------------
print(type(True))      # <class 'bool'>
print(True == 1)       # True
print(False == 0)      # True
print(True + 4)        # 5
print(False + 10)      # 10
# True behaves as 1, False behaves as 0 internally.


# ================================================================
# 🧭 Conclusion
# ================================================================
# ✔ Python numbers are dynamically typed, arbitrarily large, and precise.
# ✔ Booleans are subclasses of integers.
# ✔ Floating-point arithmetic can have rounding errors → use Decimal or Fraction.
# ✔ Operator overloading makes arithmetic expressive and flexible.
# ✔ Strong numeric foundations make Python ideal for scientific computing.
# ================================================================
