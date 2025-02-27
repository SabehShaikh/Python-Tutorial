import random

def game():
    print("You are playing the game...")
    score =random.randint(1,30)
    print(f"your score: {score}")

    # f = open("hiscore.txt", "r")
    # hiscore = f.read()
    # f.close()

    # or

    with open("hiscore.txt" , "r") as f:
        hiscore = f.read()
        # if hiscore is not empty, convert it to int
        if (hiscore != ""):
            hiscore = int(hiscore)
        # if hiscore is empty, set it to 0    
        else:
            hiscore = 0    

    if (score > hiscore):
        with open("hiscore.txt" , "w") as f:
            f.write(str(score))
        print("You have beaten the high score")
    else:
        print("You have not beaten the high score")
    print("Thanks for playing")

game()

