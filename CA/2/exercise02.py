# task :
#
# Exercise 2)
# Write a program to log in a user whose credentials are “user001” and “p455W0rd”. A user only has 3 attempts to
# log in; after this they cannot use the program. Your program should:
# • Take in the credentials from the user
# • If the user supplies valid credentials (i.e. the username and password match the values above), the user
# should see a welcome message, plus a message saying how many attempts were required to log in.
# • If the user’s credentials are invalid, the first two steps should be repeated. The user should only get 3
# attempts at logging in. After the 3rd attempt, a message should be displayed saying the user has been
# locked out, and the program should end

# storing valid credentials
user_name = "user001"
password = "p455W0rd"
attempts = 3

# storing welcome message to reuse it later
welcome = "the user name and password are correct, welcome inside this empty project full of emptiness or empty of fullness"

# creating 3 if statements to check everytime and ending with else
# getting input from user to log in
username_input = input("insert you username")
password_input = input("password")
# validating credentials
if username_input == user_name and password_input == password:
    # displaying if it is correct or not
    print(welcome, "it took you 1 attempt")
else:
    # getting input from user to log in
    username_input = input("insert you username")
    password_input = input("password")
    # validating credentials
    if username_input == user_name and password_input == password:
        # displaying if it is correct or not
        print(welcome, "it took you 2 attempts")
    else:
        # getting input from user to log in
        username_input = input("insert you username")
        password_input = input("password")
        # validating credentials
        if username_input == user_name and password_input == password:
            # displaying if it is correct or not
            print(welcome, "it took you 2 attempts")

print("you have been locked out after three attempts trying wrong password")