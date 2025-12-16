# Count alphabets and digits in file

fileptr = open("sample.txt", "r")

filecontent = fileptr.read()
alpha = 0
digits = 0

for ch in filecontent:
    if ch.isalpha():
        alpha += 1
    elif ch.isdigit():
        digits += 1

print("Number of alphabets:", alpha)
print("Number of digits:", digits)

fileptr.close()
