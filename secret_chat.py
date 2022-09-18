
# ------------------------------------FIRST_WAY----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# main_string = input()
#
# command = input()
#
# def insert_space(index, main_string):
#     return main_string[:index] + ' ' + main_string[index:]
#
# def reverse(substring, main_string):
#     word_find = main_string.find(substring)
#     main_string = main_string[:word_find] + main_string[word_find + len(substring):]
#     main_string += substring[::-1]
#     return main_string
#
# def change_all(substring, replacement, main_string):
#     return main_string.replace(substring, replacement)
#
#
# while command != "Reveal":
#     command_type, *info = command.split(":|:")
#     found_error = False
#     if command_type == "ChangeAll":
#         substring, replacement = info
#         main_string = change_all(substring, replacement, main_string)
#     else:
#         if command_type == "Reverse":
#             substring = info[0]
#             if substring not in main_string:
#                 print("error")
#                 found_error = True
#             else:
#                 main_string = reverse(substring, main_string)
#         elif "InsertSpace" == command_type:
#             index_ = int(info[0])
#             main_string = insert_space(index_, main_string)
#     if not found_error:
#         print(main_string)
#     command = input()
#
# print(f"You have a new text message: {main_string}")


# ------------------------------------SECOND_WAY----------------------------------------------------------------------------------------------------------------------------------------------------------------------


main_string = input()

command = input()

while command != "Reveal":
    type_of_command, *info = command.split(":|:")

    if type_of_command == "InsertSpace":
        index = int(info[0])

        main_string = main_string[:index] + ' ' + main_string[index:]

        print(main_string)

    elif type_of_command == "Reverse":
        substring = info[0]

        if substring in main_string:
            word_find = main_string.find(substring)

            main_string = main_string[:word_find] + main_string[word_find + len(substring):]
            main_string += substring[::-1]
            print(main_string)

        else:
            print("error")

    elif type_of_command == "ChangeAll":
        substring = info[0]
        replacement = info[1]

        if substring in main_string:
            main_string = main_string.replace(substring, replacement)

            print(main_string)

    command = input()

print(f"You have a new text message: {main_string}")