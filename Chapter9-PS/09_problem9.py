with open("file1.txt") as f:
    content1 = f.read()

with open("file2.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print("Files are identical")
else:
    print("Files are not identical")        

