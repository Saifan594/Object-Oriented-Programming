print("\033c")

class Dog:
    animal = "Dog"
    
    def __init__(self, name, age, height, weight, breed):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.breed = breed

bella = Dog("Bella", 3, 72, 29, "Golden Retriever")
leo = Dog("Leo", 4, 45, 20, "Poodle")
max = Dog("Max", 5, 60, 30, "German Shepherd")
milo = Dog("Milo", 6, 56, 36, "Labrador Retriever")
rocky = Dog("Rocky", 7, 33, 13, "French Bulldog")

print(f"Name: {bella.name}, Animal: {bella.animal}, Age: {bella.age}, Height: {bella.height}, Weight: {bella.weight}, Breed: {bella.breed}.")
print(f"Name: {leo.name}, Animal: {leo.animal}, Age: {leo.age}, Height: {leo.height}, Weight: {leo.weight}, Breed: {leo.breed}.")
print(f"Name: {max.name}, Animal: {max.animal}, Age: {max.age}, Height: {max.height}, Weight: {max.weight}, Breed: {max.breed}.")
print(f"Name: {milo.name}, Animal: {milo.animal}, Age: {milo.age}, Height: {milo.height}, Weight: {milo.weight}, Breed: {milo.breed}.")
print(f"Name: {rocky.name}, Animal: {rocky.animal}, Age: {rocky.age}, Height: {rocky.height}, Weight: {rocky.weight}, Breed: {rocky.breed}.")