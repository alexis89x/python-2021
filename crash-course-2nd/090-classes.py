class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over!")


my_dog = Dog('Nanuk', 14)
print(f"My dog name is {my_dog.name}")
my_dog.sit()


class Car:

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"this car has {self.odometer_reading}km on it")

    def increment_odometer(self, km):
        self.odometer_reading += km

    def update_odometer(self, km):
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("You can't roll back an odometer")

    def fill_gas_tank(self, liters):
        self.gas_tank += liters


my_car = Car('BMW', '218i Active Tourer', 2020)
print(my_car.get_descriptive_name())
my_car.read_odometer()
my_car.update_odometer(10000)
my_car.read_odometer()


class Battery:

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range}km on a full charge.")


class ElectricCar(Car):

    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

    def fill_gas_tank(self, liters = 0):
        print("Electric cars do not have a gas tank")

my_tesla = ElectricCar('Tesla', 'Model S', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

