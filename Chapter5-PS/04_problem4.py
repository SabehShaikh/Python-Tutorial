s = set()  # Creating an empty set

s.add(20)      # Adds integer 20 to the set
s.add(20.0)    # 20.0 (float) is numerically equal to 20 (int), so it's NOT added again
s.add("20")    # "20" (string) is different from 20 (int), so it is added separately

# Final set contains: {20, "20"}
print(len(s))  # Output: 2

# Explanation:
# - In Python, integers and floats with the same value are treated as the same key in a set.
# - 20 and 20.0 are considered equal, so only one of them is stored.
# - "20" (string) is a completely different data type from 20 (integer), so it is stored separately.
# - Therefore, the length of the set is 2.
