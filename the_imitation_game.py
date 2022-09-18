# #
# # ---------------------------------FIRST_WAY-----------------------------------------------------------------------------------------------------------------------------------------------------
# #
# # main_string = input()
# #
# # def move_string(number, string):
# #     return string[number:] + string[:number]
# #
# # def insert_string(index, value, string):
# #     return string[:index] + value + string[index:]
# #
# # def change_all(substring, replacement, string):
# #     return string.replace(substring, replacement)
# #
# # def result():
# #     print(f"The decrypted message is: {main_string}")
# #
# # command = input()
# #
# # while command != "Decode":
# #
# #     command_type, *info = [int(x) if x.isdigit() else x for x in command.split('|')]
# #
# #     if command_type == "Move":
# #         number = info[0]
# #         main_string = move_string(number, main_string)
# #
# #     else:
# #         index_or_substring, value_or_replacement = info
# #
# #         if command_type == "Insert":
# #             main_string = insert_string(index_or_substring, value_or_replacement, main_string)
# #
# #         elif command_type == "ChangeAll":
# #             main_string = change_all(index_or_substring, value_or_replacement, main_string)
# #
# #     command = input()
# #
# # result()
#
#
# # --------------------------SECOND_WAY----------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#
# encrypted_message = input()
#
# command = input()
#
# while command != "Decode":
#
#     command_type, *info = [int(x) if x.isdigit() else x for x in command.split("|")]
#
#     if command_type == "Move":
#         number_of_letters = info[0]
#         encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
#
#     elif command_type == "Insert":
#         index = info[0]
#         value = info[1]
#
#         encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
#
#     elif command_type == "ChangeAll":
#         substring = info[0]
#         replacement = info[1]
#
#         encrypted_message = encrypted_message.replace(substring, replacement)
#
#     command = input()
#
# print(f"The decrypted message is: {encrypted_message}")


 # ----------------------------THIRD_WAY----------------------------------------------------------------------------------------------------------------------------------------------------------------

main_string = input()

command = input()

while command != "Decode":

    command_type, *info = command.split("|")

    if command_type == "ChangeAll":
        substring = info[0]
        replacement = info[1]

        if substring in main_string:
            main_string = main_string.replace(substring, replacement)

    elif command_type == "Insert":
        index = int(info[0])
        value = info[1]

        main_string = main_string[:index] + value + main_string[index:]

    elif command_type == "Move":
        number_of_letters = int(info[0])

        main_string = main_string[number_of_letters:] + main_string[:number_of_letters]

    command = input()

print(f"The decrypted message is: {main_string}")