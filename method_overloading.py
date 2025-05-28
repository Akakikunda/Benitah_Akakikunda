class Calculator:
    def add(self, a, b=0, c=0):  # Overloading using default values
        return a + b + c
    
calc = Calculator()
print(calc.add(2))        # 2
print(calc.add(2, 3))     # 5
print(calc.add(2, 3, 4))  # 9

