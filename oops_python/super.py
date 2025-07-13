class Animal:
    def __init__(self):
        self.name = 'Buddy'

    def speak(self):
        print(f"{self.name} make a sound")

class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks, It is a {self.breed} dog")

dog = Dog('Labrador')
dog.speak()  # Output: Buddy make a sound
