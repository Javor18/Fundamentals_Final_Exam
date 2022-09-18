# import re
#
# main_string = input()
#
# pattern = re.compile(r'([@#])(?P<word1>[A-z]{3,})\1\1(?P<word2>[A-z]{3,})\1')
#
# result_match = []
#
# result = list(re.finditer(pattern, main_string))
#
# for match in result:
#
#     if match["word1"] == match["word2"][::-1]:
#         result_match.append(f'{match["word1"]} <=> {match["word2"]}')
#
# if result:
#     print(f"{len(result)} word pairs found!")
#
#     if result_match:
#         print("The mirror words are:")
#         print(*result_match, sep= ", ")
#
#     else:
#         print("No mirror words!")
# else:
#     print("No word pairs found!")
#     print("No mirror words!")


import re

text = input()

pattern = re.compile(r'([@#])(?P<word1>[A-z]{3,})\1\1(?P<word2>[A-z]{3,})')

words = []

result = list(re.finditer(pattern, text))

for match in result:

    if match['word1'] == match['word2'][::-1]:

        words.append(f"{match['word1']} <=> {match['word2']}")

if result:
    print(f"{len(result)} word pairs found!")

else:
    print("No word pairs found!")

if words:
    print("The mirror words are:")
    print(*words, sep= ", ")

else:
    print("No mirror words!")

