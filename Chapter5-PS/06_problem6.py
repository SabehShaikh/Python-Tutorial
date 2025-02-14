# create empty dict, allow 4 friends to
#  enter their fave lang as value
# and their names as key.

languages = {}

name = input("Enter your name: ")
language = input("Enter your favorite language: ")
languages.update({name: language})

name = input("Enter your name: ")
language = input("Enter your favorite language: ")
languages.update({name: language})

name = input("Enter your name: ")
language = input("Enter your favorite language: ")
languages.update({name: language})

name = input("Enter your name: ")
language = input("Enter your favorite language: ")
languages.update({name: language})

print(languages)



# if keys are not unique, they will be overwritten
# Values (favorite languages) can be the same, 
# so multiple people can have "Python" or "Java"
# as their favorite language.
# The dictionary allows duplicate values but not duplicate keys.
