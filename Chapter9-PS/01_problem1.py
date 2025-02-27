f = open("poems.txt", "r")

content = f.read()
if ("twinkle" in content):
    print("Twinkle is present")

else:
    print("Twinkle is not present")    


f.close()