# Python Practice - Chapter 9

This repository contains Python practice files covering **File I/O (Input/Output)**.

## Why Use Files?
- When a program runs, data is temporarily stored in **RAM (volatile memory)**.
- To store data permanently, we use **files** on the hard drive (**non-volatile memory**).
- We can **read from files** and **write to files** for data persistence.

## Types of Files:
1. **Text Files** (.txt, .py, etc.)
2. **Binary Files** (images, videos, etc.)

## Opening and Reading a File:
```python
f = open("file.txt", "r")  # Opens file in read mode by default
data = f.read()        # Reads the entire file content
print(data)
f.close()             # Always close the file after use
```

## Opening Modes:
- `r` → Read mode (default)
- `w` → Write mode (overwrites the file)
- `a` → Append mode (adds content to the end of the file)
- `rb` → Read in binary mode
- `rt` → Read in text mode
- `+` → Update mode (read + write)

## Writing to a File:
```python
st = "Hey Sabeh, you are amazing!"
f = open("myfile.txt", "w")  # Open file in write mode
f.write(st)                   # Write content to file
f.close()                     # Close file
```

## Reading Lines from a File:
```python
f = open("file.txt", "r")  # Open in read mode
lines = f.readlines()       # Reads all lines as a list
print(lines)
f.close()
```
- `.readlines()` → Reads all lines and returns a list.
- `.readline()` → Reads a single line at a time.

## Appending to a File:
```python
st = "Hey Sabeh, you are nice too."
f = open("myfile.txt", "a")  # Open in append mode
f.write(st)                   # Adds text at the end
f.close()
```

## Using `with` Statement (Recommended):
- Automatically closes the file after reading/writing.
```python
with open("file.txt", "r") as f:
    print(f.read())  # No need to explicitly close the file
```

This completes the **File I/O** chapter! 🚀

