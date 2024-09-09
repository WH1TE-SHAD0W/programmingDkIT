# random for testing
# import random

# empty list for numbers filtered from user input
numbers_taken: list = []

# the first input before while loop starts
user_input: str = input("please write down a number ")
# randomized input for testing
# user_input = str(random.randint(0,20))

# while loop that allows user take in numbers until he writes quit. The loop also separates all numbers and put them
# into list. If it is not a number, it will just notify the user of wrong input and skip it
while user_input != "quit":
    if user_input.isnumeric():
        numbers_taken.append(int(user_input))
    else:
        print("you wrote a non-numeric character")
    user_input = input("please write down a number or if you want to quit the program just write: 'quit' ")

# randomly creating numbers for testing purposes
# for i in range(random.randint(0,50)):
#     numbers_taken.append(random.randint(0,20))

# table for storing how many times has been each number wrote down. this is just created an empty list for it's
# further usage
frequency_table = []

# searching highest number inserted, respectively the limit of the loop
highest_number = 0
for number in numbers_taken:
    if number > highest_number:
        highest_number = number

# fulfilling the frequency table of numbers that has ever appeared in numbers taken list as a first column in the
# table, while the second column is the number of appearances of a certain number counted by function count
for number in range(highest_number + 1):
    row_of_table = [str(number), numbers_taken.count(number)]
    if numbers_taken.count(number) != 0:
        frequency_table.append(row_of_table)

# setting the default value of the highest number of appearances as 0 and in the loop searching what is the highest
# number
highest_frequency = 0
for row in frequency_table:
    if highest_frequency < row[1]:
        highest_frequency = row[1]

# creating list of most frequent numbers in case there are more of them
most_frequent_numbers = []

# finding the most frequent numbers in table and adding them into list
for row in frequency_table:
    if row[1] == highest_frequency:
        most_frequent_numbers.append(row)

# displaying the data of one number or more of them which have been most frequently inserted by the user
if len(most_frequent_numbers) == 1:
    print(f"the most frequent number inserted is {most_frequent_numbers[0][0]} and the amount of times you inserted "
          f"in is {most_frequent_numbers[0][1]}")
else:
    print(f"the most frequent number you inserted are: ", end="")
    for row in most_frequent_numbers:
        print(row[0], end=', ')
    print(f'this amount of time: {most_frequent_numbers[0][1]}')

# displaying the data for debug purposes
# for row in frequency_table:
#     print(row)
# print(highest_frequency)
# for row in most_frequent_numbers:
#     print(row)
