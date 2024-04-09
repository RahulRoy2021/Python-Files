# Open a file in append mode
file = open('myfile.txt', 'a')
str=input("Enter the string")
# Write some data to the file
file.write(str)

# Close the file
file.close()
