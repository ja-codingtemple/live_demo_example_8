'''
Atttributes / properties are variables inside of a class.
Methods are functions inside of a class.

Inheritance: This is the concept that allows one class to inherit the properties & methods of another class.
This creates a parent-child relationship, otherwise known as a superclass-subclass relationship.
The parent class is the superclass. It is also known as the base class.
'''
# BASE CLASS ( PARENT CLASS / SUPERCLASS )
class Animal:
    def __init__(self, name):
        self.name = name
        self.living = True
        self.legCount = 4
        self.location = "Home"
        print(f"{self.name} has been created.")
    
    def walk(self, destination):
        self.location = destination
        print(f"{self.name} walks to {self.location}.")
        
# SUBCLASSES (CHILD CLASSES) -- These inherit from the class Animal. They 'extend' Animal.
class Dog(Animal):
    def bark(self, target):
        print(f"{self.name} is barking at {target}!")
        
class Cat(Animal):
    def highjump(self, destination):
        location = destination
        print(f"{self.name} does a very high jump onto {destination}!")

'''
INSTANTIATING THE ANIMAL CLASS & ACCESSING ITS PROPERTIES / METHODS
'''
print("\nINSTANTIATING THE ANIMAL CLASS & ACCESSING ITS PROPERTIES / METHODS:")
# Create object instances of the Animal class.
animal1 = Animal("Wolf 1")
animal2 = Animal("Bear 1")
animal3 = Animal("Elk 1")

# Call the walk() method of the Animal class.
animal1.walk("the forest")
animal2.walk("the lake ")
animal3.walk("the river")

# Print out some attributes from the Animal class.
print(animal1.living)
print(animal2.living)
print(animal3.living)

'''
INSTANTIATING THE DOG & CAT SUBCLASSES & ACCESSING THEIR PROPERTIES / METHODS
'''
print("\nINSTANTIATING THE DOG & CAT SUBCLASSES & ACCESSING THEIR PROPERTIES / METHODS")
dog1 = Dog("Shadow")
dog1.walk("the dog park")
dog1.bark("the other dogs")

cat1 = Cat("Monster")
cat1.walk("the food bowl")
cat1.highjump("the kitchen counter")