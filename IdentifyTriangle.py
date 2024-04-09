side1,side2,side3=[int(side1) for side1 in input("Enter three values").split()] #Taking multiple input in one line
if ((side1+side2)>side3 and ((side1+side3)>side2) and ((side2+side3)>side3)):

    if(side1==side2 and side2==side3):
        print("Triangle is equilateral")
    elif(side1==side2 or side2==side3 or side3==side1):
        print("Triangle is isosceles")
    else:
        print("Triangle is scalene")