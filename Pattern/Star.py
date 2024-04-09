'''End parameter in the print function is used to add any string at the end of the output.
Because print function ends with a newline.
Passing the whitespace to the end parameter (end("")) indicates that the end character has to be defined by whitespace not a newline'''
row=int(input("Enter the row :"))
for i in range(1,row+1,1):
    for k in range(0,row-i,1):
        print(" ",end=(""))
    for j in range(1,2*i,1):
        print("*",end=(""))
    print()
'''for i in range(0,row):
    for k in range(0,row-i,1):
        print(" ",end=(""))
    for j in range(0,2*i+1,1):
        print("*",end=(""))
    print()'''