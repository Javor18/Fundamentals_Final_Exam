
#-----------------------------FIRST_WAY---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# import re
#
# main_string = input()
#
# pattern = re.compile(r"([#|])(?P<product_name>[A-Za-z ]+)"
#                      r"\1(?P<exp_date>[0-9]{2}\/[0-9]{2}\/[0-9]{2})"
#                      r"\1(?P<calories>[0-9]{1,5})\1")
#
# calories_last = 0
#
# result_match = []
#
# result = re.finditer(pattern, main_string)
#
# for match in result:
#
#     calories_last += int(match["calories"])
#
#     result_match.append({"item_name": match["product_name"],
#                          "expiration_date": match["exp_date"],
#                          "calories": match["calories"]})
#
# calories_last_for_day = int(calories_last / 2000)
#
# print(f"You have food to last you for: {calories_last_for_day} days!")
#
# for match in result_match:
#     print(f"Item: {match['item_name']}, Best before: {match['expiration_date']},"
#           f" Nutrition: {match['calories']}")


#-----------------------------SECOND_WAY---------------------------------------------------------------------------------------------------------------------------------------------------------------------


import re

text = input()

pattern = re.compile(r"([|#])(?P<product_name>[A-z ]+)\1"
                     r"(?P<exp_date>[0-9]{2}\/[0-9]{2}\/[0-9]{2})\1"
                     r"(?P<calories>[0-9]+)\1")

calories_last = 0
result = re.finditer(pattern, text)
result_match = []

for match in result:

    calories_last += int(match["calories"])

    result_match.append({"Product_name" : match["product_name"],
                         "expiration_date" : match["exp_date"],
                         "Calories" : match["calories"]})


days_can_survive = int(calories_last / 2000)
print(f"You have food to last you for: {days_can_survive} days!")

for product in result_match:
    print(f"Item: {product['Product_name']},"
          f" Best before: {product['expiration_date']},"
          f" Nutrition: {product['Calories']}")

# print(result_match)
