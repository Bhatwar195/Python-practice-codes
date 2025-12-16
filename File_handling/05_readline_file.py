# Read file line by line

fileptr = open("sample.txt", "r")

line1 = fileptr.readline()
line2 = fileptr.readline()

print("Line 1:", line1)
print("Line 2:", line2)

fileptr.close()
