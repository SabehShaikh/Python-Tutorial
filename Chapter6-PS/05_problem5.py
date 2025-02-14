# program to find if the given name is present in the 
# list or not:

names = ["Sabeh" , "Huzaifa" , "Shani" , "Hurri" , "Adeel"]

name = input("Enter your name: ")

if (name in names):
    print(f"Your Name {name} is present in the list.")
else:
    print("Name is not present in the list.")


