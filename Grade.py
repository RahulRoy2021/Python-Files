a,b,c,d=[int(a) for a in input("Enter Four values").split()]
avg=((a+b+c+d)/4)
print((avg))
if(avg>=75):
    print("Grade A")
elif(avg>=60):
    print("Grade B")
elif(avg>=40):
    print("Grade C")
else:
    print("Grade D")