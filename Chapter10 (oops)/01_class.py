class Employee:
    language = "Python" # class attribute
    salary = 1000 # class attribute

sabeh = Employee()
sabeh.name = "Sabeh" # object attribute
print( sabeh.name ,sabeh.salary , sabeh.language)


harry = Employee()
harry.name = "Harry" # object attribute
print( harry.name ,harry.salary , harry.language)


# here name is object attribute / instance attribute
# language and salary are class attribute
