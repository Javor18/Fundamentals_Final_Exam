import re

main_string = input()

pattern = re.compile(r"([=/])(?P<location>[A-Z][A-z]{2,})\1")

stops = []
travel_points = 0

result = re.finditer(pattern, main_string)

for match in result:

    travel_points += len(match["location"])
    stops.append(match["location"])

print(f"Destinations: {', '.join(stops)}")
print(f"Travel Points: {travel_points}")