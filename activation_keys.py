
# ---------------------------FIRST_WAY-------------------------------------------------------------------------------------------------------------------------------------------------------------

# main_string = input()
#
#
# def contains(substring, main_string):
#     if substring in main_string:
#         return f"{main_string} contains {substring}"
#     return "Substring not found!"
#
#
# def flip(type_flip, start_index, end_index, main_string):
#     if type_flip == "Upper":
#         result = main_string[:start_index] + \
#                  main_string[start_index:end_index].upper() + \
#                  main_string[end_index:]
#     elif type_flip == "Lower":
#         result = main_string[:start_index] + \
#                  main_string[start_index:end_index].lower() + \
#                  main_string[end_index:]
#     return result
#
#
# def slice_(start_index, end_index, main_string):
#     return main_string[:start_index] + main_string[end_index:]
#
#
# command = input()
#
# while command != "Generate":
#     command_name, *info = command.split(">>>")
#     if command_name == "Contains":
#         substring = info[0]
#         print(contains(substring, main_string))
#     elif command_name == "Flip":
#         type_flip, start_index, end_index = info
#         main_string = flip(type_flip, int(start_index), int(end_index), main_string)
#     elif command_name == "Slice":
#         start_index, end_index = info
#         main_string = slice_(int(start_index), int(end_index), main_string)
#     if "Contains" != command_name:
#         print(main_string)
#
#     command = input()
#
# print(f"Your activation key is: {main_string}")


# -----------------------------SECOND_WAY------------------------------------------------------------------------------------------------------------------------------------------------------------


# main_string = input()
#
# while True:
#
#     command = input().split(">>>")
#
#     command_type = command[0]
#
#     if command_type == "Generate":
#         break
#
#     elif command_type == "Contains":
#         substring = command[1]
#
#         if substring in main_string:
#             print(f"{main_stringy} contains {substring}")
#
#         else:
#             print("Substring not found!")
#
#     elif command_type == "Flip":
#
#         type = command[1]
#         start_index = int(command[2])
#         end_index = int(command[3])
#
#         if type == "Upper":
#
#             main_string = main_string[:start_index] + main_string[start_index : end_index].upper() + main_string[end_index:]
#             print(main_string)
#
#         elif type == "Lower":
#             main_string = main_string[:start_index] + main_string[start_index: end_index].lower()\
#                           + main_string[end_index:]
#             print(main_string)
#
#     elif command_type == "Slice":
#         start_index = int(command[1])
#         end_index = int(command[2])
#
#         main_string = main_string[:start_index] + main_string[end_index:]
#
#         print(main_string)
#
# print(f"Your activation key is: {main_string}")


# -----------------------------THIRD_WAY-----------------------------------------------------------------------------------------------------------------------------------------------------


main_string = input()

command = input()

while command != "Generate":

    task, *info = command.split(">>>")

    if task == "Contains":
        substring = info[0]

        if substring in main_string:
            print(f"{main_string} contains {substring}")

        else:
            print("Substring not found!")

    elif task == "Flip":

        # type = info[0]
        # start_index = int(info[1])
        # end_index = int(info[2])

        type, start_index, end_index = [int(x) if x.isdigit() else x for x in info]

        if type == "Upper":

            main_string = main_string[:start_index] + main_string[start_index:end_index].upper() + main_string[end_index:]

            print(main_string)

        elif type == "Lower":

            main_string = main_string[:start_index] + main_string[start_index:end_index].lower() + main_string[end_index:]

            print(main_string)

    elif task == "Slice":

        # start_index = int(info[0])
        # end_index = int(info[1])

        start_index, end_index = [int(x) if x.isdigit() else x for x in info]

        main_string = main_string[:start_index] + main_string[end_index:]

        print(main_string)

    command = input()

print(f"Your activation key is: {main_string}")