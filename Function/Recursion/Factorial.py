num=int(input("Enter the number"))
def factorial(a):
    if a<=1:
        return a
    else:
        return(a*factorial(a-1))
print(factorial(num))