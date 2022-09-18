
# ------------------------------------FIRST_WAY----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# number_of_plants = int(input())
#
# plants_info = {}
#
# for plant in range(number_of_plants):
#     plant_name, plant_rarity = input().split("<->")
#     plants_info[plant_name] = plants_info.get(plant_name, {})
#     plants_info[plant_name]["rarity"] = float(plant_rarity)
#     plants_info[plant_name]["rating"] = []
#
# def check_plant(plant_name):
#     if plant_name not in plants_info:
#         print("error")
#         return
#     return True
#
# def plant_rating(plant, rating):
#     if check_plant(plant):
#         plants_info[plant]["rating"].append(rating)
#
#
# def update_info(plant, new_rarity):
#     if check_plant(plant):
#         plants_info[plant]["rarity"] = new_rarity
#
#
# def reset_plant_info(plant):
#     if check_plant(plant):
#         plants_info[plant]["rating"] = []
#
#
# def show_result():
#     print("Plants for the exhibition:")
#     for plant in plants_info:
#         average_rating = 0.00
#         if sum(plants_info[plant]["rating"]) != 0:
#             average_rating = sum(plants_info[plant]["rating"]) / len(plants_info[plant]["rating"])
#         print(f"- {plant}; Rarity: {plants_info[plant]['rarity']:.0f}; Rating: {average_rating:.2f}")
#
# command = input()
#
# while command != 'Exhibition':
#
#     if 'Reset' in command:
#         _, plant = command.split(": ")
#         reset_plant_info(plant)
#         command = input()
#         continue
#
#     plant, rating_or_new_rarity = [float(x) if x.isdigit() else x for x in command.split(": ")[1].split(" - ")]
#
#     if "Rate" in command:
#         plant_rating(plant, rating_or_new_rarity)
#
#     elif "Update" in command:
#         update_info(plant, rating_or_new_rarity)
#
#     command = input()
#
# show_result()


# ------------------------------------SECOND_WAY----------------------------------------------------------------------------------------------------------------------------------------------------------------------

number_of_plant = int(input())

plants_info = {}

for plant in range(number_of_plant):
    plant_name, plant_rarity = input().split("<->")
    plants_info[plant_name] = plants_info.get(plant_name, {})
    plants_info[plant_name]["rarity"] = float(plant_rarity)
    plants_info[plant_name]["rating"] = []

command = input()

while command != "Exhibition":

        if 'Reset' in command:   #resets the rating
            _, plant_name = command.split(": ")

            if plant_name in plants_info:
                plants_info[plant_name]["rating"] = []

            else:
                print("error")


        if "Rate" in command: #append new rating

            plant_name, rating = [float(x) if x.isdigit() else x for x in command.split(": ")[1].split(" - ")]


            if plant_name in plants_info:

                plants_info[plant_name]["rating"].append(rating)

            else:
                print("error")


        elif "Update" in command: # updates the rating

            plant_name, new_rarity = [float(x) if x.isdigit() else x for x in command.split(": ")[1].split(" - ")]

            if plant_name in plants_info:

                plants_info[plant_name]["rarity"] = new_rarity

            else:
                print("error")

        command = input()

print("Plants for the exhibition:")

for plant in plants_info:
    average_rating = 0.00
    if sum(plants_info[plant]['rating']) > 0:

        print(f"- {plant}; Rarity: {plants_info[plant]['rarity']:.0f}; Rating: {(sum(plants_info[plant]['rating']) / len(plants_info[plant]['rating'])):.2f}")

    else:
        print(f"- {plant}; Rarity: {plants_info[plant]['rarity']:.0f}; Rating: 0.00")