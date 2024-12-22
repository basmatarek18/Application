class Circle:
    def __init__(self, radius):
        self._radius = radius  

    @property
    def radius(self):
        """Getter for the radius attribute."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter for the radius attribute."""
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def area(self):
        """Read-only computed attribute."""
        return 3.14159 * (self._radius ** 2)


circle = Circle(5)
print(circle.radius) 
print(circle.area)   
circle.radius = 10    
print(circle.area)    
