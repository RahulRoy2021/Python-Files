
a=float(input("Enter the 1st value :"))
b=float(input("ENter the 2nd value :"))
op=input("Enter the operation(+,-,*,/,%) You want to do :")
result=0
match op:
    case "+":
        result=a+b
        print(a,op,b,"=",result)
    case "-":
        result=a-b
        print(a,op,b,"=",result)
    case "*":
        result=a*b
        print(a,op,b,"=",result)
    case "/":
        result=a/b
        print(a,op,b,"=",result)
    case "%":
        result=a%b
        print(a,op,b,"=",result)
    case unknown_command:
        print("{0} is not valid input".format(unknown_command))


