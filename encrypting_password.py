import re

number_of_pass = int(input())

list = []

for i in range(number_of_pass):

    password = input()

    pattern = re.compile(r"(?P<start>[\S]+)>(?P<numbers>\d+)\|(?P<lower_case>[a-z]+)\|(?P<upper_case>[A-Z]+)\|(?P<symbols>[^<^>]\S+)<(?P<end>\1)(?P<valide>\S+)?")

    result = re.match(pattern, password)

    if result:

        if not result['valide']:

            print(f"Password: {result['numbers']}{result['lower_case']}{result['upper_case']}{result['symbols']}")

        else:
            print("Try another password!")

    else:
        print("Try another password!")