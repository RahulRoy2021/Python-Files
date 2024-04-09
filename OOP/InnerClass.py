class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.rollno)
    class laptop:
        def __init__(self):
            self.brand='Lenovo'
            self.cpu='i5'
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1=student("Rahul",14)
s1.show()
#1
s1.lap.show()
#2
lap1=s1.lap
lap1.show()
#3
s2=student.laptop()
s2.show()
