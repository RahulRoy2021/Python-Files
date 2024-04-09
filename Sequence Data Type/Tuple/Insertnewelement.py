names=('Vishnu','Anupama','Peter','William')
new=eval(input("Enter any string inside the bracket ():"))
pos=int(input("Enter the position"))
y=names[0:pos-1]
y=y+new
names=y+names[pos-1:]
print(names)