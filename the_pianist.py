
# ------------------------------------FIRST_WAY----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# number_of_pieces = int(input())
#
# music_info = {}
#
#
# def piece_exists(piece_name):
#     if piece_name in music_info:
#         return True
#     return False
#
#
# def add_music_info(piece_name, composer_name, key_name, first_input):
#     if piece_exists(piece_name):
#         if not first_input:
#             print(f"{piece_name} is already in the collection!")
#             return
#     if not piece_exists(piece_name):
#         music_info[piece_name] = music_info.get(piece_name, {})
#         music_info[piece_name][key_name] = composer_name
#         if not first_input:
#             print(f"{piece_name} by {composer_name} in {key_name} added to the collection!")
#
#
# def remove_music_info(piece_name):
#     if piece_exists(piece_name):
#         del music_info[piece_name]
#         print(f"Successfully removed {piece_name}!")
#         return
#     print(f"Invalid operation! {piece_name} does not exist in the collection.")
#
#
# def change_key(piece_name, key_name):
#     if piece_exists(piece_name):
#         _, name_compositor = music_info[piece_name].popitem()
#         music_info[piece_name] = {}
#         music_info[piece_name][key_name] = name_compositor
#         print(f"Changed the key of {piece_name} to {key_name}!")
#         return
#     print(f"Invalid operation! {piece_name} does not exist in the collection.")
#
#
# def show_result():
#     for piece_name in music_info:
#         for key_name, name_compositor in music_info[piece_name].items():
#             print(f"{piece_name} -> Composer: {name_compositor}, Key: {key_name}")
#
#
# for piece in range(number_of_pieces):
#     piece_name, composer_name, key_name = input().split("|")
#     add_music_info(piece_name, composer_name, key_name, True)
#
# command = input()
#
# while command != "Stop":
#     command_type, *info = command.split("|")
#     if command_type == "Remove":
#         piece_name = info[0]
#         remove_music_info(piece_name)
#     elif command_type == "Add":
#         piece_name, composer_name, key_name = info
#         add_music_info(piece_name, composer_name, key_name, False)
#
#     elif "ChangeKey" == command_type:
#         piece_name, new_key = info
#         change_key(piece_name, new_key)
#
#     command = input()
#
# show_result()


# ------------------------------------SECOND_WAY----------------------------------------------------------------------------------------------------------------------------------------------------------------------

number_of_pieces = int(input())

music_info = {}

for piece in range(number_of_pieces):

    piece_name, composer_name, key = input().split("|")

    music_info[piece_name] = music_info.get(piece_name, {})
    music_info[piece_name]["composer_name"] = composer_name
    music_info[piece_name]["key"] = key

command = input()

while command != "Stop":

    command_type, *info = command.split("|")

    if command_type == "Add":
        piece_name = info[0]
        composer_name = info[1]
        key = info[2]

        if piece_name in music_info:
            print(f"{piece_name} is already in the collection!")

        else:
            music_info[piece_name] = music_info.get(piece_name, {})
            music_info[piece_name]["composer_name"] = composer_name
            music_info[piece_name]["key"] = key
            print(f"{piece_name} by {composer_name} in {key} added to the collection!")

    elif command_type == "Remove":
        piece_name = info[0]

        if piece_name in music_info:
            print(f"Successfully removed {piece_name}!")
            del music_info[piece_name]

        else:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")

    elif command_type == "ChangeKey":

        # piece_name = info[0]
        # new_key = info[1]

        piece_name, new_key = info

        if piece_name in music_info:

            music_info[piece_name]['key'] = new_key

            print(f"Changed the key of {piece_name} to {new_key}!")

        else:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")

    command = input()

for piece_name in music_info:

    print(f"{piece_name} -> Composer: {music_info[piece_name]['composer_name']}, Key: {music_info[piece_name]['key']}")