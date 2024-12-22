class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Porsche", "mpdel")     
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")    

vehicles = [car1, boat1, plane1] 

for vehicle in vehicles:
    vehicle.move()  

