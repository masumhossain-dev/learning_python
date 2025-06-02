class Car:
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