class Person:
    __name="Rahul"
    age=19
    def talk(cls):
        print(Person.__name)
        print(cls.age)
p1=Person()
p1.talk()
print(p1._Person__name)

a=11 #11=1011

print(a.bit_length())
class p:
    def __init__(self):
        self.name="Rahul Roy"
    def show(self):
        print(self.name)
person=p()
person.show()
person2=p()
person2.show()
    