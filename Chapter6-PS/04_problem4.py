# program to find if username is less than 10 characters:


username = input("Enter your username: ")

if(len(username) < 10):
    print("Username is less than 10 characters")
    print(f"Username is: {username} , characters long: {len(username)}")
else:
    print("Username is more than 10 characters")  
    print(f"Username is: {username} , characters long: ")  