


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.color} {self.brand} is driving!")

car = Car("Tesla", "Black")
print(car.brand)
car.drive()


