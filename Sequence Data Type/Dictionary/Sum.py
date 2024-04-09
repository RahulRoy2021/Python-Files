e={}
n=int(input("Enter the number of element:"))
for i in range(n):
    k=input("Enter the key:")
    v=int(input("Enter the value"))
    e.update({k:v})
print(e)
print(sum(e.values()))
#Another way
sum=0
for i in e.values():
    if(str(i).isnumeric()):
        sum=sum+int(i)
print(sum)