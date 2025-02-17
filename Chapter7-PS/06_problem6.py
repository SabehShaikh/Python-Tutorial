n = int(input("Enter the number: "))

product = 1
for i in range(1,n+1):
    product *= i

print("The factorial of", n, "is", product)   

# Explanation:
# - The user inputs a number, which is stored in `n`.
# - The loop runs from `1` to `n+1` and multiplies the `product` with each number.
# - The `product` is initialized to `1` to start with.
# n + 1 because the loop will include `n` as well.
# - The final product is printed as the factorial of `n`.