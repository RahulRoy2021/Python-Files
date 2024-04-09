class Animal:
  def make_sound(self):
    print("Some generic animal sound")

class Cat(Animal):
  def make_sound(self):
    print("Meow")

class Dog(Animal):
  def make_sound(self):
    print("Woof")

cat = Cat()
cat.make_sound()  # prints "Meow"
a=[3,3,2,3,4]
if 3 not in a:
  print(a[-1])
dog = Dog()
dog.make_sound()  # prints "Woof"

