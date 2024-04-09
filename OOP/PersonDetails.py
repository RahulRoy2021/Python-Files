class Person:
    def __init__(self,name,gender,profession):
        self.name=name
        self.gender=gender
        self.profession=profession
    def talk(self):
        print(self.name,self.gender,self.profession)
p1=Person("John","M","Labour")
p1.talk()
p2=Person("Rahul","M","Scientist")
p2.talk()