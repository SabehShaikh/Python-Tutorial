class Employee:
    language = "Python" # class attribute
    salary = 1000 # class attribute
    
# instance attribute has higher priority:
sabeh = Employee()
sabeh.language = "JavaScript" # object attribute
print(sabeh.salary , sabeh.language)


