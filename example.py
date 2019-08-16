vehicle_database = []


class Vehicle:

    def __init__(self, model, price, color):
        self.db = VehicleDataBase()
        self.price = price
        self.model = model
        self.color = color

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def save(self):
        return self.db.insert(vehicle=self)


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


class VehicleDataBase:

    @staticmethod
    def insert(vehicle: Vehicle):
        vehicle_database.append(vehicle)

    @staticmethod
    def get_vehicles_colors():
        return [vehicle.get_color() for vehicle in vehicle_database]

    @staticmethod
    def get_under_ten_thousand_dollars():
        return [vehicle.get_model() for vehicle in vehicle_database if vehicle.get_price() < 10000]

    def get_most_common_color(self):
        filtered_list = (lambda x: x == "red", self.get_vehicles_colors())[1]
        return max(set(filtered_list), key=filtered_list.count)


def main():
    car1 = Car("Honda", 10000, "red")
    car1.save()

    car2 = Car("Ford", 20000, "red")
    car2.save()

    bike1 = Bike("Yamaha", 5000, "red")
    bike1.save()

    bike2 = Bike("Harley", 7000, "blue")
    bike2.save()

    vehicles = VehicleDataBase()

    print(f" Most common car color: {vehicles.get_most_common_color()}")

    print(f" PRICE UNDER TEN THAUSAND: {vehicles.get_under_ten_thousand_dollars()}")


main()
