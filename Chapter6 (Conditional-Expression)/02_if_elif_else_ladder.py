a = int(input("Enter your age: "))

# if elif else statement

if (a >= 18):
    print("You are eligible to vote")

elif (a < 0):
    print("you have entered negative age")

elif (a == 0):
    print("you have entered zero age")
    
else:
    print("You are not eligible to vote")    


print("End of program")