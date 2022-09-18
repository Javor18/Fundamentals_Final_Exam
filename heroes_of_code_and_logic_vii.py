
#---------------------------------------------FIRST_WAY----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# number_of_heroes = int(input())
#
# heroes_info = {}
#
# class Hero:
#
#
#     def __init__(self, name):
#         self.name = name
#         self.hp = 0
#         self.mp = 0
#
#     def add_hp(self, hp):
#         self.hp += hp
#
#     def add_mp(self, mp):
#         self.mp += mp
#
#     def cast_spell(self, needed_mp, spell_name):
#
#         if self.mp >= needed_mp:
#             self.mp -= needed_mp
#             return f"{self.name} has successfully cast {spell_name} and now has {self.mp} MP!"
#         return f"{self.name} does not have enough MP to cast {spell_name}!"
#
#     def take_damage(self, damage, attacker):
#
#         self.hp -= damage
#
#         if self.hp > 0:
#             return f"{self.name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!"
#         del heroes_info[self.name]
#         return f"{self.name} has been killed by {attacker}!"
#
#     def recharge(self, amount):
#
#         if self.mp + amount > 200:
#             amount = 200 - self.mp
#         self.mp += amount
#         return f"{self.name} recharged for {amount} MP!"
#
#     def heal(self, amount):
#
#         if self.hp + amount > 100:
#             amount = 100 - self.hp
#         self.hp += amount
#         return f"{self.name} healed for {amount} HP!"
#
#     def __repr__(self):
#         return f"{self.name}\n  " \
#                f"HP: {self.hp}\n  " \
#                f"MP: {self.mp}"
#
#
# for hero in range(number_of_heroes):
#     hero_name, hp, mp = [int(x) if x.isdigit() else x for x in input().split()]
#     heroes_info[hero_name] = heroes_info.get(hero_name, Hero(hero_name))
#     heroes_info[hero_name].add_hp(hp)
#     heroes_info[hero_name].add_mp(mp)
#
# command = input()
#
# while command != "End":
#     command_type, hero_name, *info = [int(x) if x.isdigit() else x for x in command.split(" - ")]
#
#     if command_type == "Heal":
#         hp = info[0]
#         print(heroes_info[hero_name].heal(hp))
#
#     elif command_type == "Recharge":
#         mp = info[0]
#         print(heroes_info[hero_name].recharge(mp))
#
#     elif command_type == "TakeDamage":
#         damage, attacker = info
#         print(heroes_info[hero_name].take_damage(damage, attacker))
#
#     elif command_type == "CastSpell":
#         mp_need, spell_name = info
#         print(heroes_info[hero_name].cast_spell(mp_need, spell_name))
#
#     command = input()
#
# for hero in heroes_info.values():
#     print(hero)



#-------------------------------------------SECOND_WAY----------------------------------------------------------------------------------------------------------------------------------------------------------------------


number_of_heroes = int(input())

heroes_info = {}

for hero in range(number_of_heroes):

    hero_name, hit_points, mana_points = [int(x) if x.isdigit() else x for x in input().split(" ")]

    heroes_info[hero_name] = heroes_info.get(hero_name, {})
    heroes_info[hero_name]["HP"] = hit_points
    heroes_info[hero_name]["MP"] = mana_points

command = input()

while command != "End":

    task, hero_name, *info = [int(x) if x.isdigit() else x for x in command.split(" - ")]

    if task == "CastSpell":

        # mp_needed = info[0]
        # spell_name = info[1]

        mp_needed, spell_name = info

        if heroes_info[hero_name]["MP"] >= mp_needed:

            heroes_info[hero_name]["MP"] -= mp_needed

            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_info[hero_name]['MP']} MP!")

        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif task == "TakeDamage":

        # damage = info[0]
        #
        # attacker = info[1]

        damage, attacker = info

        heroes_info[hero_name]["HP"] -= damage

        if heroes_info[hero_name]["HP"] <= 0 :

            print(f"{hero_name} has been killed by {attacker}!")

            del heroes_info[hero_name]

        else:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_info[hero_name]['HP']} HP left!")

    elif task == "Recharge":

        amount = info[0]

        if heroes_info[hero_name]["MP"] + amount > 200:

            amount = 200 - heroes_info[hero_name]["MP"]

            heroes_info[hero_name]["MP"] = 200

            print(f"{hero_name} recharged for {amount} MP!")

        else:

            heroes_info[hero_name]["MP"] += amount

            print(f"{hero_name} recharged for {amount} MP!")

    elif task == "Heal":

        amount = info[0]

        if heroes_info[hero_name]["HP"] + amount > 100:

            amount = 100 - heroes_info[hero_name]["HP"]

            heroes_info[hero_name]["HP"] = 100

            print(f"{hero_name} healed for {amount} HP!")

        else:

            heroes_info[hero_name]["HP"] += amount

            print(f"{hero_name} healed for {amount} HP!")

    command = input()

for hero in heroes_info:
    print(f"{hero}\n  " \
        f"HP: {heroes_info[hero]['HP']}\n  " \
        f"MP: {heroes_info[hero]['MP']}")