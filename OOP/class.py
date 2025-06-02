from pyexpat import model


class Car:
    # default constructor
    def __init__(self):
        self.brand = ""
        self.model = ""
        self.color = ""
        self.speed = 0

car1 = Car()
car1.brand = "Toyota"
car1.model = "X_Corolla"
car1.color = "Red"
car1.speed = 120

car2 = Car()
car2.brand = "Honda"
car2.model = "Civic"   
car2.color = "Blue"
car2.speed = 130

print(car1.brand, car1.model, car1.color, car1.speed)
print(car2.brand, car2.model, car2.color, car2.speed)


# Parameterised constructor 

class Bike:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car3 = Bike("Honda", "CBR")
print(car3.brand, car3.model)


# Default value construcot
class Bike2:
    def __init__(self, brand="Honda", model="CBR"):
        self.brand = brand
        self.model = model

car4 = Bike2()
print(car4.brand, car4.model)