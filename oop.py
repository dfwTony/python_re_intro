#loop
#object --> laptop ->
#name --> props
from numbers import result


#classes
class Person():
    def __init__(self, name, dob, color, weight, height):
        self.name = name
        self.dob = dob
        self.color = color
        self.weight = weight
        self.height = height
    def display(self):
        print(self.name)

    def get_bmi(self):
        result = self.weight / (self.height * self.height)
        return round(result, 2)

#blueprint for creating objects
p1 = Person(
    name = input("Enter your name: "),
    dob = input("Enter your date of birth: "),
    color = input("Enter your color: "),
    weight = input("Enter your weight: "),
    height = input("Enter your height: "),
)
p2 = Person(
    name = input("Enter your name: "),
    dob = input("Enter your date of birth: "),
    color = input("Enter your color: "),
    weight = input("Enter your weight: "),
    height = input("Enter your height: "),
)

p1.display()
p2.display()

print(f"{p1.name} bmi is {p1.get_bmi()} kg")
print(f"{p1.name} bmi is {p1.get_bmi()} kg")

# duplicate ctrl + d