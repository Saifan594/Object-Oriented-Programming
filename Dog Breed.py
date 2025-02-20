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

print(f"Name: {bella.name}, Animal: {bella.animal}, Age: {bella.age} yrs, Height: {bella.height} cm, Weight: {bella.weight} kg, Breed: {bella.breed}.")
print(f"Name: {leo.name}, Animal: {leo.animal}, Age: {leo.age} yrs, Height: {leo.height} cm, Weight: {leo.weight} kg, Breed: {leo.breed}.")
print(f"Name: {max.name}, Animal: {max.animal}, Age: {max.age} yrs, Height: {max.height} cm, Weight: {max.weight} kg, Breed: {max.breed}.")
print(f"Name: {milo.name}, Animal: {milo.animal}, Age: {milo.age} yrs, Height: {milo.height} cm, Weight: {milo.weight} kg, Breed: {milo.breed}.")
print(f"Name: {rocky.name}, Animal: {rocky.animal}, Age: {rocky.age} yrs, Height: {rocky.height} cm, Weight: {rocky.weight} kg, Breed: {rocky.breed}.")