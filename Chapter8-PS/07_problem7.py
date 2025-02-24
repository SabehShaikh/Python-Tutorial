# to remove a given word from list and 
# strip it at the same time

def rem(l1, word):
    n = []
    for item in l1:
        if item != word:
            n.append(item.strip(word))
    return n

l1 = ["Sabeh", "Rohit", "Babar", "Kohli", "it"]

print(rem(l1, "it"))

# explanation:
# - We first have an empty list `n` where we store our return values.
# - We loop through each item in `l1` and check if it matches `word`.
# - If the item is the word we want to remove, we skip it.
# - If not, we strip `word` from its start and end and then append it to `n`.
# - `.strip()` takes 1 argument, which is the word we want to remove.
