# task :
#
# Write a program to generate random numbers between 1 and 100. Your program should:
# • Ask the user how many random numbers to create
# • For each number created, display the number to the user and indicate if it’s odd or even
# At the end of the program, your program should display:
# • How many odd numbers were generated
# • How many even numbers were generated
# • The largest number generated
# • The average of the generated numbers

# importing function from random to be able to create random number in a ceratain range
from random import randrange

# setting up all needed variables one from input, and others to count semi calculations
# it has to be created before a loop
count: int = int(input("how many random generated numbers you want?"))
odd_numbers: int = 0
even_numbers: int = 0
maximum: int = 0
sum: int = 0

# generating a random number and initiating all required calculations in one loop and storing data in variable
for i in range(count):
    # generate number
    number = randrange(1, 100)
    # dividing number by 2 and if the remainder is 0 then it's divisible by two
    if number % 2 == 0:
        print("it's even")
        # counting even numbers
        even_numbers += 1
    elif number % 2 == 1:
        print("it's odd")
        # counting odd numbers
        odd_numbers += 1
    # if the current number is bigger than any other before it means this one is the maximum
    if maximum < number:
        maximum = number
    # counting all numbers together this is needed for the average
    sum += number
    print(number)

# calculating the average random generated number based on the sum and counted number
average = sum / count

# just displaying all information accuired
print(odd_numbers, "odd numbers were generated", even_numbers, "even numbers were generated")
print("largest number is ", maximum, "the average number is ", average)