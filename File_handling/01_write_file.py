# Write data to a file

fileptr = open("sample.txt", "w")

fileptr.write("HELLO !!")
fileptr.write("\nIt is first program of handling")

fileptr.close()

print("Data written successfully")
