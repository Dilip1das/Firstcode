class Student:
    def __init__(self):
        self.name = 'Dilip'
        self.age = 20
        self.marks = 95

    def talk(self):
        print("Name - ", self.name)
        print("age - ", self.age)
        print("marks - ", self.marks)


s1 = Student()
print(s1.name)

s1.name = "Das"
s1.talk()
print(s1.name)

s2 = Student()
print(s2.name)

# ➊ class Dog:
# ➋     """A simple attempt to model a dog."""
# ➌     def __init__(self, name, age):           """Initialize name and age attributes."""
# ➍         self.name = name           self.age = age
# ➎     def sit(self):           """Simulate a dog sitting in response to a command."""           
# print(f"{self.name} is now sitting.")       
# def roll_over(self):           """Simulate rolling over in response to a command."""           
