class Person:
  count = 0
  def __init__(self, name, age):
    self.name = name
    self.age = age

    Person.count = Person.count + 1

  def display(self):
    profile = f"My name is {self.name} and My age is {self.age}. Our head count is {self.count}"
    print(profile)

p = Person('Ali', 30)

p2 = Person('Ahmed', 20)


p2.display()
p.display()   

# print(p.name)
# print(p.age)


# print(p2.name)
# print(p2.age)

# print(type(p2))
