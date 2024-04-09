#Define a circle class allowing to create a circle with centre 'O' (A,B) and radius are using the constructor.
#Define the area method of the class which calculates the area of the circle.
#Define a parameter method of the class which allows you to calculate the perimeter of the circle.
#Define a test belongs method of the class which allows to test whether a point (x,y) belongs to the cicle or not.
import math
class circle:
    #Constructor
    def __init__(self,a,b,r):
        self.a=a
        self.b=b
        self.r=r
    def area(self):
        return math.pi*self.r**2
    def perimeter(self):
        return 2*math.pi*self.r
    def test(self,x,y):
        if(((self.a-x)**2+(self.b-y)**2==self.r**2)):
            print("The point belongs to the circle")
        else:
            print("The point does not belong to the circle")
a=circle(5,-1,3)
print(a.area())
print(a.perimeter())
a.test(2,4)