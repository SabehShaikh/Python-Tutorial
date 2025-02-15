# Python Practice - Chapter 7

This repository contains Python practice files covering **Loops**.

## Topics Covered

### Loops
Loops allow repeating a set of statements multiple times.

#### Types of Loops:
- **`while` Loop** → Runs as long as the condition is `True`.
- **`for` Loop** → Iterates over a sequence (like a list, tuple, or string).

#### `range()` Function:
- Used with `for` loops to generate a sequence of numbers.
- Syntax: `range(start, stop, step)`

### Example:
```python
# Using a for loop with range
for i in range(1, 6):
    print(i)  # Output: 1 2 3 4 5

    # Iterating over a list
l = [1, 4, 6, 234, 6, 765]
for i in l:
    print(i)

# Iterating over a tuple
t = (6, 231, 75, 90)
for i in t:
    print(i)

# Iterating over a string
s = "Sabeh"
for i in s:
    print(i)
    

# Using a while loop
x = 1
while x <= 5:
    print(x)
    x += 1
```