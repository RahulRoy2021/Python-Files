num1=int(input("Enter the num :"))
num2=int(input("Enter the power :"))

def power(a,b):
    if a==0:
        return 0
    elif b<=0:
        return 1
    else:
        return a*power(a,b-1)
value=power(num1,num2)
print(value)
