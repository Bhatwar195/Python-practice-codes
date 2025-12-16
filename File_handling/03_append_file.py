# Append data to file

fileptr = open("sample.txt", "a")

fileptr.write("\nThis line is appended")

fileptr.close()

print("Data appended successfully")
