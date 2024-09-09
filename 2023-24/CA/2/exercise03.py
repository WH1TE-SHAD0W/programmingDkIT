# task:
# Exercise 3)
# Write a program that offers two features: A number guessing game and a tax calculator. The user should be able
# to choose from either of these options repeatedly, until they enter the word “quit”.
# The guessing game should:
# • Generate a random number between 1 and 10.
# • Give the user 5 chances to guess the value.
# If they get the answer right, they should see a congratulations message, then be returned to the main
# menu to decide if they want to use the guessing game again, use the tax calculator or quit.
# • If they get the answer wrong 5 times, they should see a message saying what the number was and
# indicating that the game is over. Then they should be returned to the main menu again
# The tax calculator should:
# • Take in the user’s salary (should be greater than 0)
# • Take in the user’s tax rate (should be between 0 and 100)
# • If valid data was entered: calculate and display the yearly tax due by the user, as well as their net pay
# after taxes.
# • If invalid data was entered: inform the user that their data was inappropriate, then return them to the
# main menu.

# importing the random library
import random

user_input = input("this is the main menu choose a game or a tax calc writing down 'game' or 'tax'")
# while loop needed for getting back to main menu
while user_input != "quit":
    # match case is gonna let the user pick if he / she wants to do the game or a tax calculator or just quit the whole
    # program
    match user_input:
        case "game":
            # variables created in advance
            win_message = "that's such a great guess... you're right"
            # generating random number
            number = random.randrange(1, 10)
            # starting with one wrong answer just before the whole while loop starts
            wrong_answer = 1
            # first guess
            guess = input("guess a random generated number")
            # just a bool variable to check if it has been guessed or not
            right_answer = 0
            # while loop that lasts maximum of five times to get the number or less when it's guessed earlier
            while wrong_answer < 5 or right_answer == 1:
                # comparing the generated number with the current guess
                if number == guess:
                    # if it is right it sets the variable to 1 and displays a message
                    right_answer = 1
                    print(win_message)
                else:
                    # counting down how many wrong answer have been there
                    wrong_answer += 1
                    print("wrong")
                    # asking for another prompt
                    guess = input("guess a random generated number")
                    # if there are 5 wrong answers just another text message is displayed
                    if wrong_answer == 5:
                        print("game over")
        case "tax":
            # taking in user salary per year
            user_salary = int(input("please, insert your yearly salary"))
            # checking if it is a correct format (i would normally do it via try - catch but the tech hasn't been
            # unlocked in the tech tree)
            if user_salary <= 0:
                print("you wrote a wrong format of salary")
            else:
                # so if it's a good format then it's asks for the tax rate checks the format of tax rate and continues
                # to another commands via else
                tax_rate = int(input("please, insert your tax rate"))
                if 0 > tax_rate > 100:
                    print("you wrote a wrong format of tax rate")
                else:
                    # this just calculates the tax, net pay and after that it's printed using a f string
                    tax = user_salary * (tax_rate/100)
                    net_pay = user_salary - tax
                    print(f'your salary is {user_salary}, your tax you pay is {tax} and the net pay is {net_pay}')
    # this user input is to activate the main menu everytime again and use that match - case
    user_input = input("this is the main menu choose a game or a tax calc writing down 'game' or 'tax'")
