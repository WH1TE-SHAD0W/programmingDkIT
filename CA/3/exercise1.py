from random import randint as random
from random import shuffle as shuffle

alphabet_uppercase: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'Q',
                            'R',
                            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

alphabet_lowercase: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 'q',
                            's',
                            't', 'u', 'v', 'w', 'x', 'y', 'z']

password: list = []

for character in range(3):
    random_uppercase_character: str = alphabet_uppercase[random(0, len(alphabet_uppercase) - 1)]
    password.append(random_uppercase_character)
for character in range(5):
    random_lowercase_character: str = alphabet_lowercase[random(0, len(alphabet_lowercase) - 1)]
    password.append(random_lowercase_character)
for character in range(2):
    password.append(random(0, 9))

shuffle(password)

password_string: str = ""

for letter in password:
    password_string = password_string + str(letter)

print(password_string)
