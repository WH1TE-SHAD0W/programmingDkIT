class User:
    def __init__(self, username: str, password: str, balance: float):
        self.username = username
        self.password = password
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"The amount you requested exceeds your current balance, can't withdraw more than you have. Your "
                  f"current balance is:{self.balance}")
        else:
            auto_save(users)
            self.balance = float(self.balance) - amount
            print(f"Here is your money: {amount} bleh bleh")

    def deposit(self, amount):
        self.balance = float(self.balance) + amount
        auto_save(users)
        print(f'Thanks for your money, it\'s mine now... Your current balance is{self.balance}')

    def balance_recall(self):
        print(f'This is your balance if you are really interested heh: {self.balance}')


def sign_up(users):
    username = str(input('what is your username?'))
    password = str(input('what is your password?'))
    init_balance = input('what amount of money you want to deposit at first time?')
    if not init_balance.isdigit():
        return 'wrong input, please ensure you input only numbers'
    else:
        init_balance = float(init_balance)
    for _user in users:
        if _user.username == username:
            return 'username already taken'
    users.append(User(username, password, init_balance))
    auto_save(users)
    return 'you have been successfully signed up'


def log_in(users):
    username = str(input('what is your username?'))
    password = str(input('what is your password?'))
    global logged_in
    for _user in users:
        if _user.username == username:
            if _user.password == password:
                logged_in = True
                return _user
    print('your credentials are wrong')


def get_deposit_amount():
    amount = float(input('what amount of money you want to deposit?'))
    return amount


def get_withdraw_amount():
    amount = float(input('what amount of money you want to withdraw?'))
    return amount


def store_data(users):
    auto_save(users)
    quit()

def load_data():
    db = open("data.txt")
    data = db.readlines()
    users_from_file = []
    users = []
    for entry in data:
        entry_clear = entry.strip().split('%%')
        users_from_file.append(entry_clear)
    for _user in users_from_file:
        user = User(_user[0], _user[1], float(_user[2]))
        users.append(user)
    return users

def auto_save(users):
    # store any changes in that file
    open('data.txt', 'w').close()
    db = open("data.txt", 'w')
    for _user in users:
        db.write(f'{_user.username}%%{_user.password}%%{_user.balance}\n')
    db.close()

if __name__ == "__main__":
    users: list = load_data()
    global logged_in
    logged_in: bool = False
    quit_initiated: bool = False
    while not quit_initiated:
        if logged_in:
            print(
                'you are now logged in, if you want to withdraw money, write down "withdrawal", otherwise if you want '
                '\n'
                'to deposit any money write down "deposit" or maybe if you just want to check your balance write down '
                '"balance" and when you leavin\' don\'t forget log out writing down "log out"')
            user_input = str(input())
            match user_input:
                case "withdrawal":
                    user.withdraw(get_withdraw_amount())
                    auto_save(users)
                case "deposit":
                    user.deposit(get_deposit_amount())
                    auto_save(users)
                case "balance":
                    user.balance_recall()
                case "log out":
                    logged_in = False
                    user = ''
                case _:
                    print('sry, idk what you want, here...?')
        if not logged_in:
            # match statement if user wants to sign up or log in:
            print('choose one of following options to continue by writing the exact same:\n"log in"\n"sign up"\n"shut '
                  'down" which means also to save')
            user_input = str(input())
            match user_input:
                case "log in":
                    user = log_in(users)
                case "sign up":
                    print(sign_up(users))
                    auto_save(users)
                case "shut down":
                    store_data(users)
                case _:
                    # ask wtf he wants here
                    print("idk what you want, here...")
