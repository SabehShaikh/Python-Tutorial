# Python Practice - Chapter 8

This repository contains Python practice files covering **Functions** in Python.

## What are Functions?
- A **function** is a group of statements that perform a specific task.
- Functions **help avoid repetition** and make code **modular**.
- They are defined using the `def` keyword.

## `def` Keyword:
- The `def` keyword is used to define a function in Python.
- It is followed by the function name and parentheses `()`.
- The function body is indented and contains the code to be executed.
## Function Definition:
A function must be **defined first** before calling it.

```python
def greet():
    print("Hello, World!")  # Function body
```

## Function Call:
After defining a function, we must **call it** to execute.  
It can be called **multiple times**.

```python
greet()  # Output: Hello, World!
greet()  # Output: Hello, World! (Called again)
```

## Types of Functions:
1. **Built-in Functions** → Predefined in Python (e.g., `print()`, `len()`, `type()`)
2. **User-defined Functions** → Functions created by the user.

```python
# Built-in Function Example
print(len("Hello"))  # Output: 5

# User-defined Function Example
def say_hello():
    print("Hello, Python!")

say_hello()
```

## Functions with Arguments:
Functions can **take parameters** to work with different values.

```python
def goodDay(name):
    print(f"Good day, {name}!")

goodDay("Sabeh")  # Output: Good day, Sabeh!
```

## `return` Keyword:
The `return` statement is used to **send a value back** from the function.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

## Default Parameters:
We can set a **default value** for function parameters.

```python
def goodDay(name, ending="Thank you!"):
    print(f"Good day {name}, {ending}")

goodDay("Ronaldo")  # Output: Good day Ronaldo, Thank you!
goodDay("Babar", "See you soon!")  # Output: Good day Babar, See you soon!
```

## Recursion:
A **recursive function** is a function that **calls itself**.  
Recursion is useful for problems like **factorial calculation, Fibonacci sequence, and tree traversal**.

```python
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else: 
        return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of {n} is {factorial(n)}")
```

---

This README provides a **clear and structured** explanation of Python functions. 🚀  

