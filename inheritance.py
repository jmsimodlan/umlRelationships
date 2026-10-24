class Animal:
    def speak(self):
        print("An animal makes a sound.")


class Dog(Animal):
    def bark(self):
        print("The dog says: Woof!")


# Create an object
dog = Dog()

# Use the inherited method
dog.speak()

# Use the child's own method
dog.bark()
