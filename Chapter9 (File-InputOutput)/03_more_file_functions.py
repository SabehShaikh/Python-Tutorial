f = open("file.txt" , "r")

# lines = f.readlines()
# print(lines)
# f.close()

line = f.readline()
while line != "":
    print(line)
    line = f.readline()

f.close()    