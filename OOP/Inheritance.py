#Single Inheritance
class Father:
    def __init__(self,property):
        self.property=property
    def display_property(self):
        print("Father's property-",self.property)
class Son(Father):
    def __init__(self,property1,property):
        super().__init__(property)
        self.property1=property1
    def display_property(self):
        super().display_property()
        print("Total Property of child=",self.property+self.property1)
s=Son(200000.00,300000.00)
Father.display_property(s)#To access the property of father class
print('Son\'s property',s.property1)#To access the class of Son
Son.display_property(s)
#OR
s.display_property()
#Multiple Inheritance
class father:
    def height(self):
        print("Height is 6.0 Foot")
class mother:
    def color(self):
        print("Color is brown")
class child(father,mother):
    pass
c=child()
print("Child's inherited qualities")
c.height()
c.color()
