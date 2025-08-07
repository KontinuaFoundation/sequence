dog1name = "Teddy"
dog1age = 6
dog1sound = "woof"

dog2name = "Fluffers"
dog2age = 2
dog2sound = "bark"

dog3name = "Bella"
dog3age = 3
dog3sound = "grr"

print(f"{dog1name} is {dog1age} and says {dog1sound}!")
print(f"{dog2name} is {dog2age} and says {dog2sound}!")
print(f"{dog3name} is {dog3age} and says {dog3sound}!")

# ====================================================
# object oriented model with class dog

class Dog:
    """A simple model of a dog."""
    # constructor - which creates a new model of a dog. 
    def __init__(self, name: str, age: int, sound: str):
        self.name = name
        self.age = age
        self.sound = sound
    # method speak 
    def speak(self) -> None:
        """Print a sentence describing the dog."""
        print(f"{self.name} is {self.age} and says {self.sound}!")

# create dog objects called “instances” with the given variables
dog1 = Dog("Teddy", 6, "woof")
dog2 = Dog("Fluffers", 2, "bark")
dog3 = Dog("Bella", 3, "grr")

# call the behavior on each object
dog1.speak()
dog2.speak()
dog3.speak()