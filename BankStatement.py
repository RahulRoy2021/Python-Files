
amount=0
while(True):
    a,b=[str(i) for i in input().split(" ")]
    value=int(b)
    if a=="D":
        amount=amount+value
    elif a=="W":
        if(value<amount):
            amount=amount-value
        else:
            print("Balance amount is less,so no withdrawal")
    elif a=="E":
        break
    else:
        print("enter valid input")   
print(amount)

