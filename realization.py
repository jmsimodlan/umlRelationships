from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    # Implement the required abstract method
    def speak(self):
        print("The dog says: Woof!")


# Create an object of the implementing class
dog = Dog()
dog.speak()
