class Animal:
    def speak(self):
        return'some sound'
    
class Dog(Animal):
    def speak(self):
        return "Bark"
    
class Cat (Animal):
    def speak(self):
        return "Meow"
    
animals = [Dog(), Cat(), Animal()]

sounds = [animal.speak() for animal in animals]

