#hiding internal details and showing only essential features 

#abc=abstraction based classes
from abc import ABC, abstractmethod

#ABSTRACT CLASS
class Animal(ABC):
    @abstractmethod
    def make_sound(): 
        pass #pass represents null value

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

lion = Lion()
lion.make_sound()

cow=Cow()
cow.make_sound()