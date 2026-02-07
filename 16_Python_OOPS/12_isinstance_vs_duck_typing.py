# ============================================================
# isinstance vs Duck Typing
# ============================================================

# Both approaches are used to determine how an object
# should be handled, but they differ fundamentally.

# ------------------------------------------------------------
# isinstance (Type-Based Checking)
# ------------------------------------------------------------
# isinstance checks whether an object is an instance
# of a specific class or its subclasses.

class FileLogger:
    def write(self, message):
        print(message)

class SocketLogger:
    def write(self, message):
        print(message)

def log_with_isinstance(logger):
    if isinstance(logger, FileLogger):
        logger.write("File log")
    elif isinstance(logger, SocketLogger):
        logger.write("Socket log")
    else:
        raise TypeError("Unsupported logger type")

# ------------------------------------------------------------
# Duck Typing (Behavior-Based Checking)
# ------------------------------------------------------------
# Duck typing focuses on behavior, not type.
# If an object implements the required method, it is accepted.

def log_with_duck_typing(logger):
    logger.write("Log entry")

log_with_duck_typing(FileLogger())
log_with_duck_typing(SocketLogger())

# ------------------------------------------------------------
# Comparison
# ------------------------------------------------------------
# isinstance:
# - Rigid
# - Tightly coupled to class hierarchy
# - Harder to extend
#
# Duck typing:
# - Flexible
# - Loosely coupled
# - Easier to extend
#
# Python favors duck typing in most cases.
