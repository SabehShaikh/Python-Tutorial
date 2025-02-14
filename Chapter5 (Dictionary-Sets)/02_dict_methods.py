marks = {
    "Sabeh" : 100,
    "Rahim" : 75,
    "Karim" : 56,
    0 : "hello"
}

print(marks.items())

# give all the keys
print(marks.keys())

# give all the values
print(marks.values())

# updates existing values also
# adds new values
marks.update({
    "Rahim" : 80,
    "Asim": 90
})

print("updated: ",marks)

# if key is not present > returns None
print(marks.get("Sabeh"))

# if key is not present > returns error
print(marks["Sabeh"])

# deletes the value
marks.pop("Rahim")
print(marks)

# deletes the last value
marks.popitem()
print(marks)
     
