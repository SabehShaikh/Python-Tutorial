# Chapter 10: Object-Oriented Programming (OOP)

## Introduction to OOP
Object-Oriented Programming (OOP) is a programming paradigm that solves problems by creating objects. It follows the **DRY (Don't Repeat Yourself)** principle, which emphasizes reusability and modularity.

---

## Class: Blueprint for Creating Objects
A **class** is a blueprint for creating objects. It defines the structure and behavior of objects.

### Example:
Think of a class as a form:
- When the form is empty, it is just a blueprint (class).
- When someone fills the form, it becomes their form (object).

Similarly, a single class can create multiple objects, just like a single form can be filled by multiple participants.

---

## Object: Instance of a Class
An **object** is an instance of a class. It represents a specific entity with its own attributes and methods.

### Example:
- **Noun (Class):** `Employee`
- **Adjectives (Attributes):** `name`, `age`, `salary`
- **Verbs (Methods):** `getSalary()`

---

## Class Attributes
Class attributes are attributes that belong to the class itself rather than a specific object. They are shared across all instances of the class.

### Example:
```python
class Employee:
    language = "Python"  # Class attribute
    salary = 1000        # Class attribute

# Creating objects
sabeh = Employee()
sabeh.name = "Sabeh"  # Object attribute
print(sabeh.name, sabeh.salary, sabeh.language)  # Output: Sabeh 1000 Python

harry = Employee()
harry.name = "Harry"  # Object attribute
print(harry.name, harry.salary, harry.language)  # Output: Harry 1000 Python
```

---

## Instance Attributes vs Class Attributes
Instance attributes have higher priority than class attributes. If an instance attribute is defined, it will override the class attribute.

### Example:
```python
class Employee:
    language = "Python"  # Class attribute
    salary = 1000        # Class attribute

sabeh = Employee()
sabeh.language = "JavaScript"  # Object attribute
print(sabeh.salary, sabeh.language)  # Output: 1000 JavaScript
```

---

## The `self` Parameter
The `self` parameter refers to the instance of the class. It is used to access class attributes and methods.

### Example:
```python
class Employee:
    language = "Python"  # Class attribute
    salary = 1000        # Class attribute

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

sabeh = Employee()
sabeh.language = "JavaScript"  # Object attribute
sabeh.getInfo()  # Output: The language is JavaScript and the salary is 1000
```

---

## Static Methods
Static methods are methods that do not require the `self` parameter. They are not dependent on the class or instance.

### Example:
```python
class Employee:
    @staticmethod
    def greet():
        print("Good morning!")

Employee.greet()  # Output: Good morning!
```

---

## `__init__` Constructor (Dunder Method)
The `__init__` method is a special method that runs automatically when an object is created. It is used to initialize object attributes.

### Example:
```python
class Employee:
    language = "Python"  # Class attribute
    salary = 1000        # Class attribute

    def __init__(self):
        print("This is the constructor. It will run automatically.")
        self.name = "Sabeh"

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning!")

sabeh = Employee()
print(sabeh.name)  # Output: This is the constructor. It will run automatically. Sabeh
```

---

## Parameterized Constructor
You can also pass parameters to the `__init__` method to initialize object attributes dynamically.

### Example:
```python
class Employee:
    def __init__(self, name, language, salary):
        print("This is the constructor. It will run automatically.")
        self.name = name
        self.language = language
        self.salary = salary

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning!")

sabeh = Employee("Sabeh", "JavaScript", 2500)
print(f"The name of the employee is {sabeh.name} and the salary is {sabeh.salary}")
# Output: The name of the employee is Sabeh and the salary is 2500
```

---

## Summary
- **Class:** A blueprint for creating objects.
- **Object:** An instance of a class.
- **Class Attributes:** Shared across all instances of the class.
- **Instance Attributes:** Specific to each object.
- **self Parameter:** Refers to the instance of the class.
- **Static Methods:** Do not require `self` and are independent of the class/instance.
- **`__init__` Constructor:** Automatically runs when an object is created.

---

## Example Code
```python
class Employee:
    language = "Python"  # Class attribute
    salary = 1000        # Class attribute

    def __init__(self, name, language, salary):
        print("This is the constructor. It will run automatically.")
        self.name = name
        self.language = language
        self.salary = salary

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning!")

# Creating objects
sabeh = Employee("Sabeh", "JavaScript", 2500)
sabeh.getInfo()  # Output: The language is JavaScript and the salary is 2500
sabeh.greet()    # Output: Good morning!
```

---

This concludes Chapter 10 on Object-Oriented Programming. Happy coding! 🚀
