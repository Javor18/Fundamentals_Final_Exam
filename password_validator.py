password = input()

command = input()

uppercase = 0
lowercase = 0
digits = 0
p = 0

while command != "Complete":

    # task, *info = [int(x) if x.isdigit() else x for x in command.split(" ")]
    #
    # print(task)
    # print(info)

    if "Make Upper" in command:
        command = command.split(" ")

        index = int(command[2])
        word = password[index]

        password = password[:index] + word.upper() +password[index + 1:]

        print(password)

    elif "Make Lower" in command:

        command = command.split(" ")

        index = int(command[2])
        word = password[index]

        password = password[:index] + word.lower() + password[index + 1:]

        print(password)

    elif "Insert" in command:

        command = command.split(" ")

        index = int(command[1])
        char = command[2]

        if 0 <= index < len(password):

            password = password[:index] + char + password[index:]

            print(password)

    elif "Replace" in command:

        command = command.split(" ")

        char = command[1]
        value = int(command[2])

        if char in password:

            ascii_char_value = ord(char)

            ascii_char_value += value

            symbol = chr(ascii_char_value)

            password = password.replace(char, symbol)

            print(password)

    elif "Validation" in command:

        if len(password) < 8:

            print("Password must be at least 8 characters long!")

        for character in password:

            if character.isalpha() or character.isdigit() or character == "_":
                p += 1

            else:
                print("Password must consist only of letters, digits and _!")

            if character.isupper():
                uppercase += 1

            if character.islower():
                lowercase += 1

            if character.isdigit():
                digits += 1

        if uppercase == 0:
            print("Password must consist at least one uppercase letter!")

        if lowercase == 0:
            print("Password must consist at least one lowercase letter!")

        if digits == 0:
            print("Password must consist at least one digit!")

    command = input()