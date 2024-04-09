'''num=int(input("enter the number :"))
length=(len(str(num)))
temp=num
sum=0
while temp!=0:
    r=temp%10
    sum=sum+(r**length)
    temp//=10
if sum==num:
    print("The number is armstrong")
else:
    print("Number is not armstrong")'''
#Find the armstrong number between the given limit
min,max=[int (i) for i in input("enter the min & max").split()]
while min<=max:
    temp=min
    sum=0
    while temp!=0:
        r=temp%10
        sum=sum+(r**len(str(min)))
        temp//=10
    if sum==min:
        print("{0} is armstrong number".format(min))
    min+=1