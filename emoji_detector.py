import re


main_string = input()

pattern = r'([0-9])|(\*{2}[A-Z][a-z]{2,}\*{2})|(\:{2}[A-Z][a-z]{2,}\:{2})'

result = re.finditer(pattern, main_string)

words = {}

cool_threshold = 1

for match in result:

    word = match.group()

    if word.isdigit():
        cool_threshold *= int(word)

    else:
        words[word] = 0

        for character in word:

            if character != ":" and character != "*":
                words[word] += ord(character)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(words)} emojis found in the text. The cool ones are:")

for word in words:
    if words[word] >= cool_threshold:
        print(word)