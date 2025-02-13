name = "Sabeh Shaikh"
print(len(name))

print(name.endswith("ikh")) # True

print(name.startswith("sa")) # false cuz sa != Sa

print(name.startswith("Sa")) # true

# only the first letter is capitalized
print(name.capitalize())

# first letter of each word is capitalized
print(name.title())

# all letters are converted to lowercase
print(name.lower())

# all letters are converted to uppercase
print(name.upper())

# replace a string with another string
print(name.replace("Shaikh", "Shah"))

# find the index of a string
print(name.find("a"))