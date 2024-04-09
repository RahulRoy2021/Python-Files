'''num=int(input("Enter the number "))
temp=num
sum=0
while(temp):
    i=1
    r=temp%10
    fact=1
    while(i<=r):
        fact=fact*i
        i+=1
    sum=sum+fact
    temp=temp//10
if(num==sum):
    print("the number is strong")
else:
    print("The number is not strong")
'''

min=int(input("Min"))
max=int(input("Max"))
for check in range(min,max+1,1):
    temp=check
    sum=0
    for i in range(0,len(str(check))):
        r=temp%10
        fact=1
        for i in range(1,r+1):
            fact=fact*i
        sum=sum+fact
        temp=temp//10
    if(check==sum):
        print("The number {0} is strong\n".format(check))

