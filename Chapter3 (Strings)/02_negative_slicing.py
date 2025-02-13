name = "Sabeh"
print(name[0:3])

# negative slicing (start from the end)
print(name[-4: -1]) # same as name[1:4]

# start from index 1 and end at index 4 (not including 4)
print(name[1:4]) 

# start from the beginning and end at index 2 (excluding 2)
print(name[:2]) # same as name[0:2]

# start from index 2 and end at the end 
print(name[2:]) # same as name[2:len(name)]