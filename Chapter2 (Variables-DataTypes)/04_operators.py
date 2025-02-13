# Arithmetic Operators

a = 20
b = 10
c = a + b
print(c)



# Assignment Operators
a = 4-2
print(a)
b = 6
b += 3 # increments b by 3 and assign it to b
print(b)

b -= 3 # decrements b by 3 and assign it to b
print(b)

b *= 3 # multiplies b by 3 and assign it to b
print(b)

b /= 3 # divides b by 3 and assign it to b
print(b)

# Comparison Operators

d = 5 < 4 # 5 is not less than 4, so false
print(d)

e = 5 > 4 # 5 is greater than 4, so true
print(e)

f = 5 == 4 # 5 is not equal to 4, so false
print(f)

g = 5 != 4 # 5 is not equal to 4, so true
print(g)

# Logical operators

h = True or False # or stops at the first true
print(h) # only one of them has to be true

# Truth table of 'or' 
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'and' 
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

# Truth table of 'not' , negation
print(not(True)) # False
print(not(False)) # True