# ============================================================
# Python Dunder (Magic) Methods – COMPLETE REFERENCE
# ============================================================

# Dunder methods:
#   - Special methods surrounded by double underscores
#   - Automatically invoked by Python
#   - Enable operator overloading, iteration, context managers,
#     attribute access, object creation, and more
#
# You DO NOT call these directly.
# Python calls them for you.

# ============================================================
# Object Creation & Lifecycle
# ============================================================

__new__(cls, *args, **kwargs)
# Called BEFORE __init__
# Responsible for creating the object
# Used mainly in immutable types and metaclasses

__init__(self, *args, **kwargs)
# Object initializer (constructor)

__del__(self)
# Destructor (called when object is garbage-collected)
# ⚠️ Not reliable for critical cleanup

# ============================================================
# String / Representation Methods
# ============================================================

__str__(self)
# Called by str(obj), print(obj)
# Human-readable representation

__repr__(self)
# Called by repr(obj), interactive shell
# Developer-friendly, unambiguous representation

__format__(self, format_spec)
# Used by format() and f-strings

__bytes__(self)
# Called by bytes(obj)

# ============================================================
# Comparison (Rich Comparison Methods)
# ============================================================

__eq__(self, other)   # ==
__ne__(self, other)   # !=
__lt__(self, other)   # <
__le__(self, other)   # <=
__gt__(self, other)   # >
__ge__(self, other)   # >=

# ============================================================
# Arithmetic Operators
# ============================================================

__add__(self, other)        # +
__sub__(self, other)        # -
__mul__(self, other)        # *
__truediv__(self, other)   # /
__floordiv__(self, other)  # //
__mod__(self, other)       # %
__pow__(self, other)       # **
__matmul__(self, other)    # @

# Reflected (right-hand) operations
__radd__(self, other)
__rsub__(self, other)
__rmul__(self, other)
__rtruediv__(self, other)
__rfloordiv__(self, other)
__rmod__(self, other)
__rpow__(self, other)
__rmatmul__(self, other)

# In-place operations
__iadd__(self, other)
__isub__(self, other)
__imul__(self, other)
__itruediv__(self, other)
__ifloordiv__(self, other)
__imod__(self, other)
__ipow__(self, other)
__imatmul__(self, other)

# ============================================================
# Unary Operators
# ============================================================

__neg__(self)    # -obj
__pos__(self)    # +obj
__abs__(self)    # abs(obj)
__invert__(self) # ~obj

# ============================================================
# Type Conversion
# ============================================================

__int__(self)
__float__(self)
__complex__(self)
__bool__(self)
__index__(self)   # Used for slicing & binary operations

# ============================================================
# Attribute Access Control
# ============================================================

__getattr__(self, name)
# Called when attribute NOT found

__getattribute__(self, name)
# Called for EVERY attribute access (dangerous if misused)

__setattr__(self, name, value)
# Called when setting attributes

__delattr__(self, name)
# Called when deleting attributes

__dir__(self)
# Controls output of dir(obj)

# ============================================================
# Container / Collection Behavior
# ============================================================

__len__(self)
# len(obj)

__getitem__(self, key)
# obj[key]

__setitem__(self, key, value)
# obj[key] = value

__delitem__(self, key)
# del obj[key]

__contains__(self, item)
# item in obj

# ============================================================
# Iteration Protocol
# ============================================================

__iter__(self)
# Returns iterator

__next__(self)
# Returns next item

# ============================================================
# Callable Objects
# ============================================================

__call__(self, *args, **kwargs)
# Makes object callable like a function

# ============================================================
# Context Managers (with statement)
# ============================================================

__enter__(self)
# Enter context

__exit__(self, exc_type, exc_val, exc_tb)
# Exit context (handles exceptions)

# ============================================================
# Hashing & Identity
# ============================================================

__hash__(self)
# Used in sets and dict keys

__eq__(self, other)
# Must be consistent with __hash__

# ============================================================
# Pickling & Copying
# ============================================================

__copy__(self)
__deepcopy__(self, memo)

__getstate__(self)
__setstate__(self, state)

__reduce__()
__reduce_ex__()

# ============================================================
# Class & Metaclass Hooks
# ============================================================

__class_getitem__(cls, item)
# Enables Generic[T] syntax

__init_subclass__(cls, **kwargs)
# Called when subclass is created

__mro_entries__(self, bases)
# Affects multiple inheritance

# ============================================================
# Async / Await Support
# ============================================================

__await__(self)

__aiter__(self)
__anext__(self)

__aenter__(self)
__aexit__(self)

# ============================================================
# Descriptor Protocol
# ============================================================

__get__(self, instance, owner)
__set__(self, instance, value)
__delete__(self, instance)

# Used in:
#   - @property
#   - ORM fields
#   - Validators

# ============================================================
# Numeric & Bitwise Operations
# ============================================================

__and__(self, other)   # &
__or__(self, other)    # |
__xor__(self, other)   # ^
__lshift__(self, other) # <<
__rshift__(self, other) # >>

__rand__(self, other)
__ror__(self, other)
__rxor__(self, other)
__rlshift__(self, other)
__rrshift__(self, other)

__iand__(self, other)
__ior__(self, other)
__ixor__(self, other)
__ilshift__(self, other)
__irshift__(self, other)

# ============================================================
# Summary (Interview Gold)
# ============================================================

# - Dunder methods define how objects behave
# - Python syntax is powered by these hooks
# - Operator overloading is NOT magic — it’s __add__, etc.
# - Iteration, context managers, properties, async — all dunder
# - You only implement what you need
# - Overusing them = unreadable code

# ============================================================
# Rule of Thumb
# ============================================================

# Implement when behavior is natural and intuitive
# Avoid clever tricks that surprise readers
