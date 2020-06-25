class Salary:
    def __init__(self,pay,reward):
        self.pay = pay
        self.reward = reward

    def annual_salary(self):
        return (self.pay*12)+self.reward


class Employee:
    def __init__(self,name,position,sal):
        self.name = name
        self.position = position
        self.final_salary = sal

    def final_salary_m(self):
        return self.final_salary.annual_salary()

sal = Salary(100000,10000)


emp = Employee("Dilip", "py Dev",sal)
print(emp.final_salary_m())

class MyClass:
    x = 5
print(MyClass)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])