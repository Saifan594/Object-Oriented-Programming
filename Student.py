print("\033c")

class student:
    grade = 7
    print(f"Hi I am in grade {grade}")
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

saifan = student("Saifan", 13)
nahian = student("Nahian", 28)

print(saifan.grade)
print(nahian.grade)

print(f"My name is {saifan.name} and my age is {saifan.age}")
print(f"My name is {nahian.name} and my age is {nahian.age}")