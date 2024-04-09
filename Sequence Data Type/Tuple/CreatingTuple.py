tup=eval(input("Enter the elements within the bracket ():"))
print(tup)
#Inserting:
new,pos=[int (i) for i in input("Enter the value you want to store and position").split()]
new=tuple([new])
y=tup[0:pos-1]
y=y+new
tup=y+tup[pos-1:]
print(tup)
#Modify:
new,pos=[int (i) for i in input("Enter the value you want to store and position").split()]
new=tuple([new])
y=tup[0:pos-1]
y=y+new
tup=y+tup[pos:]
print(tup)
#Delete:
pos=int(input("Enter the position"))
y=tup[0:pos-1]
tup=y+tup[pos:]
print(tup)