# program to print multiplication table of a
#  given number using for loop:

num = int(input("Enter the number you want the multiplication table of: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

