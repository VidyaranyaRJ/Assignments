# Single Inheritance
class Animal:
    def sound(self):
        return "Animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

# Multiple Inheritance
class Bird:
    def fly(self):
        return "Flying"

class Parrot(Dog, Bird):
    def speak(self):
        return "Chirp"

# Multilevel Inheritance
class Person:
    def greet(self):
        return "Hello"

class Employee(Person):
    def work(self):
        return "Working"

class Manager(Employee):
    def manage(self):
        return "Managing"


dog = Dog()
print(dog.sound())

parrot = Parrot()
print(parrot.sound(), parrot.fly())

manager = Manager()
print(manager.greet(), manager.work(), manager.manage())
