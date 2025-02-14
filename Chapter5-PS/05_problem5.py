s = {}

# what is the type of s?
print(type(s)) # Output: <class 'dict'>

# Explanation:
# - In Python, {} (curly braces) by default creates an empty dictionary, NOT a set.
# - A dictionary is a collection of key-value pairs, but since no key-value pairs are provided, it remains empty.
# - To create an empty set, we must use `set()` instead of `{}`.
# - Example of an empty set: s = set()