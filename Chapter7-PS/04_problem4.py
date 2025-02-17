# Program to check if the number is prime or not

# A prime number is only divisible by 1 and itself.

num = int(input("Enter the number you want the multiplication table of: "))

for i in range(2, num):  # Loop starts from 2 to num-1
    if num % i == 0:  # If num is divisible by i
        print(f"{num} is not a prime number")  # It is not a prime number
        break  # Exit the loop
else:
    print(f"{num} is a prime number")  # If loop completes, num is prime

# Explanation:
# - The user inputs a number, which is stored in `num`.
# - The loop runs from `2` to `num-1` and checks if `num` is divisible by any number in this range.
# - If `num` is divisible by any `i`, it prints "not a prime number" and exits (`break`).
# - If no divisor is found, the loop completes and the `else` block executes, printing "is a prime number".

# Example 1: Input = 7
# Iteration:
#   - 7 % 2 != 0
#   - 7 % 3 != 0
#   - 7 % 4 != 0
#   - 7 % 5 != 0
#   - 7 % 6 != 0
#   - Since no divisor found, "7 is a prime number" is printed.

# Example 2: Input = 6
# Iteration:
#   - 6 % 2 == 0 (divisible by 2, so not prime)
#   - Prints "6 is not a prime number" and exits loop.

# Key Concept:
# - The `else` in a loop runs **only if the loop completes without a `break`**.
# - If `break` occurs (meaning a divisor was found), `else` does **not** run.
