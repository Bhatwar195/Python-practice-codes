# Read file in bytes

fileptr = open("sample.txt", "r")

print(fileptr.read(32))   # reads first 32 characters

fileptr.close()
