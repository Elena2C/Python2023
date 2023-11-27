class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return self.towing_capacity


car = Car("Toyota", "Camy", 2020, 12)
motorcycle = Motorcycle("Honda", "CBaaaRR", 2013, 20)
truck = Truck("Ford", "Fhh150", 2012, 1000)

print(f"{car.get_description()} has a mileage of {car.calculate_mileage(300)} kilometers per liter.")
print(f"{motorcycle.get_description()} has a mileage of {motorcycle.calculate_mileage(200)} kilometers per liter.")
print(f"{truck.get_description()} has a towing capacity of {truck.calculate_towing_capacity()} tons.")
