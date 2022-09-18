#
# # ------------------------------------FIRST_WAY----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# # number_of_cars = int(input())
# #
# # car_info = {}
# #
# # class Car:
# #
# #     def __init__(self, name):
# #         self.name = name
# #         self.mileage = 0
# #         self.fuel = 0
# #
# #
# #     def add_mileage(self, mileage):
# #         self.mileage += mileage
# #
# #
# #     def add_fuel(self, fuel):
# #         self.fuel += fuel
# #
# #
# #     def drive(self, distance, need_fuel):
# #         if self.fuel < need_fuel:
# #             print("Not enough fuel to make that ride")
# #         else:
# #             self.mileage += distance
# #             self.fuel -= need_fuel
# #             print(f"{self.name} driven for {distance} kilometers. {need_fuel} liters of fuel consumed.")
# #
# #             if self.mileage >= 100_000:
# #                 print(f"Time to sell the {self.name}!")
# #                 del car_info[self.name]
# #
# #     def refuel(self, fuel):
# #         if self.fuel + fuel > 75:
# #             fuel = 75 - self.fuel
# #         self.fuel += fuel
# #         print(f"{self.name} refueled with {fuel} liters")
# #
# #     def revert(self, kilometers):
# #         self.mileage -= kilometers
# #         if self.mileage < 10_000:
# #             self.mileage = 10_000
# #             return
# #         print(f"{self.name} mileage decreased by {kilometers} kilometers")
# #
# # #_repr_ -> създава данните в car_info
# #
# #     def __repr__(self):
# #         return f"{self.name} -> Mileage: {self.mileage} kms, Fuel in the tank: {self.fuel} lt."
# #
# #
# # for car in range(number_of_cars):
# #     car_name, mileage, fuel = [int(x) if x.isdigit() else x for x in input().split("|")]
# #     car_info[car_name] = car_info.get(car_name, Car(car_name))
# #     car_info[car_name].add_mileage(mileage)
# #     car_info[car_name].add_fuel(fuel)
# #
# # command = input()
# #
# # while command != "Stop":
# #     command_type, car_name, *info = [int(x) if x.isdigit() else x for x in command.split(" : ")]
# #     if command_type == "Drive":
# #         distance, fuel = info
# #         car_info[car_name].drive(distance, fuel)
# #     elif command_type == "Refuel":
# #         fuel = info[0]
# #         car_info[car_name].refuel(fuel)
# #     elif command_type == "Revert":
# #         kilometers = info[0]
# #         car_info[car_name].revert(kilometers)
# #     command = input()
# #
# #
# # for car in car_info.values():
# #     print(car)
#
#
# # ------------------------------------SECOND_WAY----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# number_of_cars = int(input())
# car_info = {}
#
# for car in range(number_of_cars):
#
#     car_name, mileage, fuel_available = [int(x) if x.isdigit() else x for x in input().split("|") ]
#
#     car_info[car_name] = car_info.get(car_name, {})
#     car_info[car_name]["mileage"] = mileage
#     car_info[car_name]["fuel_available"] = fuel_available
#
# command = input()
#
# while command != "Stop":
#
#     command = command.split(" : ")
#
#     if command[0] == "Drive":
#         car_name = command[1]
#         distance = int(command[2])
#         needen_fuel = int(command[3])
#
#         if car_info[car_name]["fuel_available"] < needen_fuel:
#             print("Not enough fuel to make that ride")
#
#         else:
#             car_info[car_name]["fuel_available"] -= needen_fuel
#             car_info[car_name]["mileage"] += distance
#             print(f"{car_name} driven for {distance} kilometers. {needen_fuel} liters of fuel consumed.")
#
#             if car_info[car_name]["mileage"] >= 100_000:
#                 print(f"Time to sell the {car_name}!")
#                 del car_info[car_name]
#
#     elif command[0] == "Refuel":
#         car_name = command[1]
#         fuel = int(command[2])
#
#         if  car_info[car_name]["fuel_available"] + fuel > 75:
#             add_fuel = 75 - car_info[car_name]["fuel_available"]
#             car_info[car_name]["fuel_available"] += add_fuel
#             print(f"{car_name} refueled with {add_fuel} liters")
#
#         else:
#             car_info[car_name]["fuel_available"] += fuel
#             print(f"{car_name} refueled with {fuel} liters")
#
#     elif command[0] == "Revert":
#         car_name = command[1]
#         mileage_to_dicrease = int(command[2])
#
#         car_info[car_name]["mileage"] -= mileage_to_dicrease
#
#         if car_info[car_name]["mileage"] < 10_000:
#
#             car_info[car_name]["mileage"] = 10_000
#
#         else:
#             print(f"{car_name} mileage decreased by {mileage_to_dicrease} kilometers")
#
#     command = input()
#
# for car_name in car_info:
#     print(f'{car_name} -> Mileage: {car_info[car_name]["mileage"]} kms, Fuel in the tank: { car_info[car_name]["fuel_available"]} lt.')


#------------------------------------------THIRD_WAY----------------------------------------------------------------------------------------------------------------------------------------------------------------------


number_of_cars = int(input())

car_info = {}

for car in range(number_of_cars):

    car_name, mileage, fuel = [int(x) if x.isdigit() else x for x in input().split("|")]

    car_info[car_name] = car_info.get(car_name, {})

    car_info[car_name]["mileage"] = mileage

    car_info[car_name]["fuel_available"] = fuel

command = input()

while command != "Stop":

    task, *info = command.split(" : ")

    if task == "Drive":

        # car_name = info[0]
        # distance = int(info[1])
        # needen_fuel = int(info[2])

        car_name, distance, needen_fuel = [int(x) if x.isdigit() else x for x in info]

        if car_info[car_name]["fuel_available"] < needen_fuel:
            print("Not enough fuel to make that ride")

        else:
            car_info[car_name]["mileage"] += distance
            car_info[car_name]["fuel_available"] -= needen_fuel

            print(f"{car_name} driven for {distance} kilometers. {needen_fuel} liters of fuel consumed.")

        if car_info[car_name]["mileage"] >= 100_000:

            print(f"Time to sell the {car_name}!")

            del car_info[car_name]

    elif task == "Refuel":

        # car_name = info[0]
        # fuel = int(info[1])

        car_name, fuel = [int(x) if x.isdigit() else x for x in info]

        if car_info[car_name]["fuel_available"] + fuel > 75:

            fuel = 75 - car_info[car_name]["fuel_available"]

            car_info[car_name]["fuel_available"] = 75

            print(f"{car_name} refueled with {fuel} liters")

        else:
            car_info[car_name]["fuel_available"] += fuel
            print(f"{car_name} refueled with {fuel} liters")

    elif task == "Revert":

        # car_name = info[0]
        # kilometers = int(info[1])

        car_name, kilometers = [int(x) if x.isdigit() else x for x in info]

        car_info[car_name]["mileage"] -= kilometers

        if car_info[car_name]["mileage"] < 10_000:

            car_info[car_name]["mileage"] = 10_000

        else:
            print(f"{car_name} mileage decreased by {kilometers} kilometers")

    command = input()

for car in car_info:

    print(f"{car} -> Mileage: {car_info[car]['mileage']} kms, Fuel in the tank: {car_info[car]['fuel_available']} lt.")