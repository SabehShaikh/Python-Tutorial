for i in range(100):
    if(i == 34):
        break #exit the loop
    print(i)

for i in range(100):
    if(i == 34):
       continue #skip this iteration
    print(i)    

for num in range(1, 6):
    if num == 3:
        print("Three found!")
    elif num == 5:
        print("Five found!")
    else:
        print(num)