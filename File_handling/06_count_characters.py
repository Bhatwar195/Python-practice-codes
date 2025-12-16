# Count total characters in file

fileptr = open("sample.txt", "r")

filecontent = fileptr.read()
count = 0

for ch in filecontent:
    count += 1

print("Total number of characters:", count)

fileptr.close()
