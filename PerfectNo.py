num=int(input("Enter the integer:"))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
if(sum==num):
    print("Number is perfect")
else:
    print("Number is not perfect")