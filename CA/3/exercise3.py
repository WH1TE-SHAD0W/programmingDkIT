import random

numbers_taken = []
user_input = input()
# user_input = str(random.randint(0,20))

while user_input != "quit":
    if user_input.isnumeric():
        numbers_taken.append(int(user_input))
    else:
        print("you wrote a non-numeric character")
    user_input = input()

# for i in range(random.randint(0,50)):
#     if user_input.isnumeric():
#         numbers_taken.append(int(user_input))
#     else:
#         print("you wrote a non-numeric character")
#     # user_input = input()
#     user_input = str(random.randint(0,20))
frequency_table = []

highest_number = 0
for number in numbers_taken:
    if number > highest_number:
        highest_number = number

for number in range(highest_number):
    row_of_table = [str(number), numbers_taken.count(number)]
    if numbers_taken.count(number) != 0:
        frequency_table.append(row_of_table)

highest_frequency = 0
for row in frequency_table:
    if highest_frequency < row[1]:
        highest_frequency = row[1]

most_frequent_numbers = []

for row in frequency_table:
    if row[1] == highest_frequency:
        most_frequent_numbers.append(row)

if len(most_frequent_numbers) == 1:
    print(f"the most frequent number inserted is {most_frequent_numbers[0][0]} and the amount of times you inserted "
          f"in is {most_frequent_numbers[0][1]}")
else:
    print(f"the most frequent number you inserted are: ", end="")
    for row in most_frequent_numbers:
        print(row[0], end=', ')
    print(f'this amount of time: {most_frequent_numbers[0][1]}')

# print(frequency_table)
# print(highest_frequency)
# print(most_frequent_numbers)
