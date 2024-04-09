print("The Form of the quadratic equation is ax**2+bx+c=0")
import math #Only the sqrt function is imported
a=float(input("Enter the value of a"))
b=float(input("Enter the value of b"))
c=float(input("enter the value of c"))
if(a==0):
    print("value of a should not be zero")
else:
    delta=(b*b-4*a*c)
    if(delta<0):
        print("The roots are not real")
    elif(delta==0):
        root=(-b/2*a)
        print(root)
    else:
        root1=(-b+math.sqrt(delta))/(2*a)
        root2=(-b-math.sqrt(delta))/(2*a)
        print("Equation has two roots.")
        print("The roots are ",root1,root2)