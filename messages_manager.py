
records = {}

capacity_of_possible_messages = int(input())

command = input()

while command != "Statistics":

    task, *info = [int(x) if x.isdigit() else x for x in command.split("=")]

    if task == "Add":

        username, sent, received = info

        if username not in records:

            records[username] = records.get(username, {})
            records[username]["sent_messages"] = sent
            records[username]["received_messages"] = received

    elif task == "Message":

        sender, receiver = info

        if sender in records and receiver in records:

            records[sender]["sent_messages"] += 1

            records[receiver]["received_messages"] += 1

            if records[sender]["sent_messages"] + records[sender]["received_messages"] == capacity_of_possible_messages:

                print(f"{sender} reached the capacity!")

                del records[sender]

            if records[receiver]["received_messages"] + records[receiver]["sent_messages"]  == capacity_of_possible_messages:

                print(f"{receiver} reached the capacity!")

                del records[receiver]

    elif task == "Empty":

        username = info[0]

        if username in records:

            del records[username]

        if username == "All":

            records = {}


    command = input()


print(f"Users count: {len(records)}")

for person in records:

    print(f"{person} - {records[person]['sent_messages'] + records[person]['received_messages']}")