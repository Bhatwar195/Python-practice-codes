# Count special symbols in file

fileptr = open("sample.txt", "r")

filecontent = fileptr.read()
alphanumeric = 0
special = 0

for ch in filecontent:
    if ch.isalnum():
        alphanumeric += 1
    else:
        special += 1

print("Alphanumeric characters:", alphanumeric)
print("Special symbols:", special)

fileptr.close()
