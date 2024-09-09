# importing libraries as variables from random
from random import randint as random
from random import shuffle as shuffle

# creating a list of characters from alphabet one is uppercase and the other is lowercase so, I don't need to use
# string functions to lowercase or to uppercase any letter later on
alphabet_uppercase: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'Q',
                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

alphabet_lowercase: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 'q',
                            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# creating an empty list for password
password: list = []

# loop for implementing 3 uppercase character, it takes a random number which is used as an index to access a letter
# from the list and append it to the end of a password list of characters the same logic is done on the other two
# loops but with different characters (lowercase and number) and different amount of cycles so, it's gonna just put
# different amount of characters to the password. Just to mention the last loop is not accessing any list, it generates
# number characters automatically
#
# complaining: due to the restrictions, there's no other option just to use random list indexing. Well, I'd like to
# use functions such as chr()
for character in range(3):
    random_uppercase_character: str = alphabet_uppercase[random(0, len(alphabet_uppercase) - 1)]
    password.append(random_uppercase_character)
for character in range(5):
    random_lowercase_character: str = alphabet_lowercase[random(0, len(alphabet_lowercase) - 1)]
    password.append(random_lowercase_character)
for character in range(2):
    password.append(random(0, 9))

# not sure if it is illegal or not but it makes no difference in the program requirements. It will shuffle all the
# password characters and make it even more random
shuffle(password)

# for list to string converting I created a new variable called password string and basically in the loop down I am
# just adding all character from password variable into one string trough a for loop.
password_string: str = ""

for letter in password:
    password_string = password_string + str(letter)

# displaying the password completely
print(password_string)
