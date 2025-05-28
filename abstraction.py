# Abstraction
from abc import ABC, abstractmethod #abstraction

#dealing with Animals 
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass #the method sound has no implementation
    
#child class implementing the abstract method
class Dog(Animal):
    def sound():
        print('Dog makes a barking sound')
        
class Pig(Animal):
    def sound():
        print('Pig makes a oink  sound')
        
#we cannot create objects of an abstract class
#like 
#Animal1 = Animal() it brings errors
# we can create objects of child or sub class like 
#Dog1 = Dog()
#Pig1 = Pig()

#displaying output or calling the method
Dog.sound()
Pig.sound()

#class Dog:
  #  def sound(self):
 #       print("Bark")

#my_dog = Dog()   # 🐶 Make a dog
#my_dog.sound()   # ✅ Call sound on that dog

