class Animal():
    def sound():
        print('Animal make sound ')
    
class Dog(Animal):
    def sound():
        print('Dog makes a barking sound')
        
class Pig(Animal):
    def sound():
        print('Pig makes a oink  sound')
        
Animal.sound()
Dog.sound()
Pig.sound()


class Calculator:
    def add(self, a, b=0, c=0):  # Overloading using default values
        return a + b + c
    
calc = Calculator()
print(calc.add(2))        # 2
print(calc.add(2, 3))     # 5
print(calc.add(2, 3, 4))  # 9

