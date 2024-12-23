class Vehicle:
    def description(self):
        return "This is a vehicle."

class Car(Vehicle):
    def description(self):
        return "This is a car."

class Truck(Vehicle):
    def description(self):
        return "This is a truck."

vehicle = Vehicle()
car = Car()
truck = Truck()

print(vehicle.description())  
print(car.description())  
print(truck.description()) 
