# ============================================================
# Designing Polymorphic APIs
# ============================================================

# A polymorphic API:
# - Accepts different object types
# - Works with a common interface or behavior
# - Does not depend on concrete implementations

# ------------------------------------------------------------
# Poor Design (Type Checking Everywhere)
# ------------------------------------------------------------
def process_payment(payment):
    if isinstance(payment, CreditCard):
        payment.pay()
    elif isinstance(payment, UPI):
        payment.pay()
    else:
        raise TypeError("Unsupported payment type")

# This design:
# - Breaks extensibility
# - Requires modification for every new type

# ------------------------------------------------------------
# Better Design (Polymorphism)
# ------------------------------------------------------------
class PaymentMethod:
    def pay(self):
        raise NotImplementedError

class CreditCard(PaymentMethod):
    def pay(self):
        print("Paid using credit card")

class UPI(PaymentMethod):
    def pay(self):
        print("Paid using UPI")

def process_payment(payment: PaymentMethod):
    payment.pay()

process_payment(CreditCard())
process_payment(UPI())

# ------------------------------------------------------------
# Pythonic Polymorphic API (Duck Typing)
# ------------------------------------------------------------
def process_payment(payment):
    payment.pay()

# Any object with a pay() method is supported.

# ------------------------------------------------------------
# Design Guidelines
# ------------------------------------------------------------
# - Depend on behavior, not concrete types
# - Avoid isinstance checks when possible
# - Use abstract base classes for formal contracts
# - Prefer duck typing for lightweight APIs
# - Keep APIs open for extension, closed for modification
