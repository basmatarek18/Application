# Method Overloading Simulation Example

class Calculator:
    def add(self, a, b=None):
        if b is not None:
            return a + b
        else:
            return a + a  

calc = Calculator()

print(calc.add(3, 5))  

print(calc.add(3))  
