class Car:
    all_cars = dict()

    @classmethod
    def remove_car(cls, car_to_remove):
        del cls.all_cars[car_to_remove]
        print(f'Time to sell the {car_to_remove}!')

    def __init__(self, _car: str, _mileage: int, _fuel: int):
        self.car = _car
        self.mileage = _mileage
        self.fuel = _fuel

    def __repr__(self):
        return f"{self.car} -> Mileage: {self.mileage} kms, Fuel in the tank: {self.fuel} lt."

    def drive(self, _distance, _fuel):
        if _fuel <= self.fuel:
            self.mileage += _distance
            self.fuel -= _fuel
            print(f"{self.car} driven for {_distance} kilometers. {_fuel} liters of fuel consumed.")
            if self.mileage >= 100_000:
                Car.remove_car(self.car)
        else:
            print('Not enough fuel to make that ride')

    def refuel(self, _fuel):
        if _fuel + self.fuel > 75:
            _fuel = 75 - self.fuel
        print(f"{self.car} refueled with {_fuel} liters")
        self.fuel += _fuel

    def revert(self, _kilometers):
        if self.mileage - _kilometers >= 10_000:
            self.mileage -= _kilometers
            print(f"{self.car} mileage decreased by {_kilometers} kilometers")
        else:
            self.mileage = 10_000


amount = int(input())

for _ in range(amount):
    car, mileage, fuel = input().split('|')
    current_car = Car(car, int(mileage), int(fuel))
    Car.all_cars[car] = current_car

while True:
    cmd = input().split(' : ')
    if cmd[0] == 'Stop':
        break
    elif cmd[0] == 'Drive':
        Car.all_cars[cmd[1]].drive(int(cmd[2]), int(cmd[3]))
    elif cmd[0] == 'Refuel':
        Car.all_cars[cmd[1]].refuel(int(cmd[2]))
    elif cmd[0] == 'Revert':
        Car.all_cars[cmd[1]].revert(int(cmd[2]))

for current_car in Car.all_cars.values():
    print(current_car)