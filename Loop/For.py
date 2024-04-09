min,max=[int (i) for i in input("Enter the min term and max term \n").split()]
for i in range(min,max+1):
    temp1=i
    flag=0
    for j in range(1,len(str(i))+1):
        temp=i%10
        if(temp==5):
            flag+=1
        i=i//10
    if(len(str(temp1))==flag):
        print(temp1)


      
city=["Kolkata","Pune","Goa"]
length=len(city)
for i in range(length):
    print("I love",city[i])