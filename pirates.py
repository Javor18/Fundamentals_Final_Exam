command = input()
sail_destinations = {}

while command != "Sail":
    data = command.split("|")

    city_name = data[0]
    population = int(data[2])
    gold = int(data[4])

    if city_name in sail_destinations:
        sail_destinations[city_name]["population"] += population
        sail_destinations[city_name]["gold"] += gold

    else:

        sail_destinations[city_name] = sail_destinations.get(city_name, {})
        sail_destinations[city_name]["population"] = population
        sail_destinations[city_name]["gold"] = gold

    command = input()

task = input()

while task != "End":

    task_type , *info = [int(x) if x.isdigit() else x for x in task.split("=>")]

    if task_type == 'Plunder':

        # town = info[0]
        # people = info[1]
        # gold = info[2]

        town, people, gold = info

        if sail_destinations[town]["population"] > 0 or sail_destinations[town]["gold"] > 0:
            sail_destinations[town]["population"] -= people
            sail_destinations[town]["gold"] -= gold
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")


        if sail_destinations[town]["population"] == 0 or sail_destinations[town]["gold"] == 0:

            print(f"{town} has been wiped off the map!")
            del sail_destinations[town]

    elif task_type == 'Prosper':

        town = info[0]
        gold_added = int(info[1])

        if gold_added < 0:
            print(f"Gold added cannot be a negative number!")

        else:
            sail_destinations[town]["gold"] += gold_added
            print(f'{gold_added} gold added to the city treasury. {town} now has {sail_destinations[town]["gold"]} gold.')

    task = input()

if len(sail_destinations) > 0:
    print(f"Ahoy, Captain! There are {len(sail_destinations)} wealthy settlements to go to:")

    for city in sail_destinations:
        print(f'{city} -> Population: {sail_destinations[city]["population"]} citizens, Gold: {sail_destinations[city]["gold"]} kg')

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")