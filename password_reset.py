#
# # --------------------------  FIRST_WAY  ----------------------------------------------------------------------------------------------------------
#
#
# # main_string = input()
# #
# # command = input()
# #
# # def take_odd(main_string):
# #     return "".join(main_string[i] for i in range(len(main_string)) if i % 2 != 0)
# #
# # def cut_string(index, length, main_string):
# #     return main_string[:index] + main_string[(index + length):]
# #
# # def substitute(substring, substitute, main_string):
# #     return main_string.replace(substring, substitute)
# #
# #
# # while command != "Done":
# #     nothing_to_replace = False
# #     if command[0] == "TakeOdd":
# #         main_string = take_odd(main_string)
# #
# #     else:
# #         task, index_or_substring, length_or_substitute = [int(x) if x.isdigit() else x for x in command.split()]
# #
# #         if task == "Cut":
# #             main_string = cut_string(index_or_substring, length_or_substitute, main_string)
# #
# #         elif task == "Substitute":
# #             if index_or_substring in main_string:
# #                 main_string = substitute(index_or_substring, length_or_substitute, main_string)
# #             else:
# #                 print("Nothing to replace!")
# #                 nothing_to_replace = True
# #
# #     if not nothing_to_replace:
# #         print(main_string)
# #
# #     command = input()
# #
# # print(f"Your password is: {main_string}")
#
# # --------------------------  SECOND_WAY  ----------------------------------------------------------------------------------------------------------
#
#
# def password_reset():
#     main_string = input()
#
#     while True:
#
#         command = input().split(" ")
#
#         if command[0] == "Done":
#             break
#
#         else:
#
#             if  command[0] == "TakeOdd":
#                 main_string = ''.join(main_string[i] for i in range(len(main_string)) if i % 2 != 0)
#                 print(main_string)
#
#             elif  command[0] == "Cut":
#                 index = int(command[1])
#                 length = int(command[2])
#                 main_string = ''.join(main_string[i] for i in range(len(main_string))
#                                       if i < index or i >= index + length)
#                 print(main_string)
#
#             elif  command[0] == "Substitute":
#
#                 substring = command[1]
#                 substitute = command[2]
#
#                 if substring in main_string:
#                     main_string = main_string.replace(substring, substitute)
#                     print(main_string)
#
#                 else:
#                     print("Nothing to replace!")
#
#     print(f'Your password is: {main_string}')
#
# password_reset()
# print()


# ---------------------------  THIRD_WAY  ----------------------------------------------------------------------------------------------------------


main_string = input()

command = input()

while command != "Done":

    if command == "TakeOdd":

        main_string = "".join(main_string[i] for i in range(len(main_string)) if i % 2 != 0)
        print(main_string)

    else:
        task, *info = command.split(" ")

        if task == "Cut":

            # index = int(info[0])
            # length = int(info[1])

            index,length = [int(x) if x.isdigit() else x for x in info]

            main_string = main_string[:index] + main_string[index + length:]
            print(main_string)

        elif task == "Substitute":

            # substring = info[0]
            # substitute = info[1]

            substring, substitute = info

            if substring in main_string:

                main_string = main_string.replace(substring, substitute)

                print(main_string)

            else:
                print("Nothing to replace!")

    command = input()

print(f"Your password is: {main_string}")
