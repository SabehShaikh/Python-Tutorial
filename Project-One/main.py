import random
'''
1 for snake
-1 for water 
0 for gun
'''
computer = random.choice([-1, 0, 1])  # Computer randomly selects Snake (1), Water (-1), or Gun (0)

youstr = input("Enter your choice: ")  # e.g., if we enter "s", then youstr = "s"

youDict = {"s": 1, "w": -1, "g": 0}  # Maps user input to corresponding values: Snake = 1, Water = -1, Gun = 0

reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}  # Maps numeric values back to their names for printing

you = youDict[youstr]  # Converts user input into a numeric value, e.g., youDict["s"] → 1
# Now `you = 1` if we chose "s" (Snake)

# reverseDict[1] = "Snake", which helps in printing the result later


# By now we have 2 numbers (variables), 
# you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer ==-1 and you == 1): 
        print("You win!")

    elif(computer ==-1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer ==1 and you == 0):
        print("You Win!")

    elif(computer ==0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")