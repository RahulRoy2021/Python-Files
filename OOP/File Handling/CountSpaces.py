f=open("MyFile.txt","r")
'''count=0
while True:
    char=f.read(1)
    if char==" ":
        count+=1
    if not char:
        break
print(count)'''
#Another way
ch=f.read()
count=0
for i in ch:
    if i==" ":
        count+=1
print(count)
f.seek(0)
print(f.tell())
f.close()