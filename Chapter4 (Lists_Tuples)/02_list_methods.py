friends = ["Apple" , "Orange" , 5 , False, "Banana" , 34.5]
print("Original list: ", friends)

# to add element at the end
friends.append("Mango")
print("list after append: ", friends)

# to sort in ascending order (small to big)
l1 = [2,64,25,35,30,11]
l1.sort()
print(l1)

# to sort in descending order (big to small)
l2 = [2,64,25,35,40,11]
l2.sort(reverse=True)
print(l2)

# to reverse
l3 = [64,20,30,45,55,16]
l3.reverse()
print(l3)

# to insert element at specific index
l3.insert(2, 25) # insert 25 at index 2
print(l3)

# to remove element at specific index
l3.pop(2) # remove element at index 2
print(l3)

# to remove specific element
l3.remove(64) # remove 64 from the list
print(l3)