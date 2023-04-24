# Membuat sebuah Class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, speed_increase):
        self.speed += speed_increase

    def brake(self, speed_decrease):
        self.speed -= speed_decrease

    def current_speed(self):
        return self.speed

# Membuat Instance/Object dari Class Car
my_car = Car("Toyota", "Corolla", 2021)

# Memanggil Method pada Object
my_car.accelerate(50)
print(my_car.current_speed()) # Output: 50

my_car.brake(20)
print(my_car.current_speed()) # Output: 30
