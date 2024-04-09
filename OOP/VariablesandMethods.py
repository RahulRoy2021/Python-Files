class Student:
    school="Adamas" #Class(Static) Variable
    def __init__(self,n1,n2,n3):
        self.n1=n1
        self.n2=n2   #Instance Variable
        self.n3=n3
    #Instance Method
    def avg(self):
        return (self.n1+self.n2+self.n3)/3
    #Class Method
    @classmethod
    def info(cls):
        print(cls.school)
    #Static Method
    @staticmethod
    def classinfo():
        print("This is a student class")
s1=Student(23,45,67)
s2=Student(34,56,24)
print(s1.avg())
print(s2.avg())
s1.info()
s2.info()
Student.info()
Student.classinfo()
s1.classinfo()
Student.school="TBHS" #Modify the static(class) variable
Student.info() #To access class method
s1.n1=32 #Modify the instance variable
print(s1.avg())