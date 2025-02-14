a = int(input("Enter your age: "))

# if statement no 1:
if (a % 2 == 0):
    print("The number is even")

# end of if statement 1    

# if statement no 2:
if (a >= 18):
    print("You are eligible to vote")

elif (a < 0):
    print("you have entered negative age")

elif (a == 0):
    print("you have entered zero age")
    
else:
    print("You are not eligible to vote")  

# end of if statement 2      


print("End of program")