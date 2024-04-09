def sum(a,b):
    c=a+b
    return c
def substraction(a,b):
    c=a-b
    return c
def multi(a,b):
    c=a*b
    return c
def division(a,b):
    c=a/b
    return c
x,y=[int(i) for i in input("Enter Two values").split()]
s=sum(x,y)
subs=substraction(x,y)
Multi=multi(x,y)
div=division(x,y)
print("Sum {0}".format(s),"Substraction",subs,"Multiplication",Multi,"Division",div)