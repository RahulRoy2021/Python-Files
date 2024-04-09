class Employee:
    __count=0
    def __init__(self):
        Employee.__count+=1
    def display(self):
        print("The no. of employees",Employee.__count)
emp=Employee()
emp1=Employee()
print(emp._Employee__count)
try:
    print(emp.__count)
except AttributeError:
    print('There is an attribute error')
finally:
    emp.display()