# create a class with a class attribute a
# create an object from it and set 'a' directly using object.a = 0
# does this change the class attribute a?

# ANSWER IS NO

class Test:
    a = 1  # Class attribute

t = Test()   # Create an instance
t.a = 0      # Create an instance attribute (shadows class attribute)

print(t.a)    # Prints 0 (instance attribute is accessed)
print(Test.a) # Prints 1 (class attribute remains unchanged)
