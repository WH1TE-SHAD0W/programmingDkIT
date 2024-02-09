# make a table for users, columns : username, password, account_balance out of the so-called DB that is the text file
# here, where are those entries stored
db = open("data.txt")
data = db.readlines()
users = []
open('data.txt', 'w').close()
for entry in data:
    entry_clear = entry.strip().split('%%')
    users.append(entry_clear)

logged_in: bool = False

# program:
#  do it all the time, (if statements can't be referenced)
while True:
    # if user is logged in:
    if logged_in:
        print('you are now logged in, if you want to withdraw money, write down "withdrawal", otherwise if you want \n'
              'to deposit any money write down "deposit" or maybe if you just want to check your balance write down '
              '"balance" and when you leavin\' don\'t forget log out writing down "log out"')
        user_input = str(input())
        # match statement to get what user want:
        match user_input:
            # in case it is withdrawal:
            case "withdrawal":
                # ask how much, subtract it from account and get him the money
                withdraw_amount = input("how much do you want to withdraw")
                # check if he has enough
                if deposit_amount >= users[2][(users[0].index(user))]:
                    users[2][(users[0].index(user))] = - float(withdraw_amount)
                    print("here are you money, bleh bleh")
                else:
                    print("you don\'t have enough")
            # in case it is deposit:
            case "deposit":
                # ask how much, add it to account and get the money from him
                deposit_amount = input("how much do you want to withdraw")
                users[2][(users[0].index(user))] = + float(deposit_amount)
                print(f'thanks for your money, mnam mnam... your balance is now {users[2][(users[0].index(user))]}')
            # in case it is to check balance:
            case "balance":
                # tell him how poor he is
                print(f" your bank account balance is : ${users[2][(users[0].index(user))]} you are very poor, sorry")
            # in case he wants to log out:
            case "log out":
                # log out and say bye bye
                print("bye bye see ya")
                logged_in = False
            # in case it is something else:
            case _:
                # tell hime wtf he wants, I have no idea...
                print("I kinda don't know what you want from me")
    # if user is not logged in:
    if not logged_in:
        # match statement if user wants to sign up or log in:
        print('if you want to log in write down "log in" otherwise if you want to sign up write down "sign up"')
        user_input = str(input())
        match user_input:
            # in case he wants to log in:
            case "log in":
                #     ask what is his username
                username = input("what is your username?")
                #     ask what is his password
                password = input("what is your password?")
                #     if it is correct:
                for _username in users[0]:
                    if _username == username and users[1][users[0].index(_username)]:
                        # log him in
                        user = _username
                        logged_in = True
                        print("log in was successful")
                # if wrong say your credentials are wrong
                if not logged_in:
                    print("your credentials are wrong")
            # in case he wants to sign up:
            case "sign up":
                #     ask for username
                username = input("what is your username?")
                #     ask for password
                password = input("what is your password?")
                #     make a new row in table of users with username, password and account balance of 0
                users[0].append(username)
                users[1].append(password)
                users[2].append(float(0))
            case "shut down":
            #     store any changes in that file
                db = open("data.txt", 'w')
                for _user in users:
                    db.write(f'{_user[0]}%%{_user[1]}%%{_user[2]}\n')
                db.close()
                        # in any other case:
            case _:
                #     ask wtf he wants here
                print("idk what you want, here...")

