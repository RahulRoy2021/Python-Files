def add(farg,*args):#Variable length argument
    print('Formal argument :',farg)
    sum=0
    for i in args:
        sum=sum+i
    print('Sum is :',(farg+sum))
add(6,7,8,9)