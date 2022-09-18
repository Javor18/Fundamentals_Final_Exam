
# -----------------------------------FIRST_WAY--------------------------------------------------------------------------------------------------------------------------------------------------------------------

list_of_stops = input()

command = input()

while command != "Travel":

    task, *info = command.split(":")

    # print(task)
    # print(info)


    if task == "Add Stop":

        # index = int(info[0])
        # string = info[1]

        index, string = [int(x) if x.isdigit() else x for x in info]

        if 0 <= index < len(list_of_stops):
            list_of_stops = list_of_stops[:index] + string + list_of_stops[index:]

    elif task == "Remove Stop":
         # start_index = int(info[0])
         # end_index = int(info[1])

         start_index, end_index = [int(x) if x.isdigit() else x for x in info]

         if (0 <= start_index < len(list_of_stops)) and (0 <= end_index < len(list_of_stops)):
            list_of_stops = list_of_stops[:start_index] + list_of_stops[end_index + 1:]

    elif task == "Switch":
        # old_string = info[0]
        # new_string = info[1]

        old_string, new_string = info

        if old_string in list_of_stops:
            list_of_stops = list_of_stops.replace(old_string, new_string)

    print(list_of_stops)
    command = input()

print(f"Ready for world tour! Planned stops: {list_of_stops}")


# -----------------------------------SECOND_WAY---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# data = input()
# command = input()
#
# while not command == 'Travel':
#
#     command = command.split(":")
#
#     if command[0] == 'Add Stop':
#
#         index = int(command[1])
#         string = command[2]
#
#         if 0 <= index < len(data):
#             data = data[:index] + string + data[index:]
#
#     elif command[0] == 'Remove Stop':
#
#         start_index = int(command[1])
#         end_index = int(command[2])
#
#         if (0 <= start_index < len(data)) and (0 <= end_index < len(data)):
#             data = data[:start_index] + data[end_index + 1:]
#
#     elif command[0] == 'Switch':
#
#         old_str = command[1]
#         new_str = command[2]
#
#         if old_str in data:
#             data = data.replace(old_str, new_str)
#
#     print(data)
#     command = input()
#
# print(f"Ready for world tour! Planned stops: {data}")