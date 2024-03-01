from exercise_1 import verify_email
from os import path


def email_verification(recipient_email):
    email_not_valid: bool = True
    while email_not_valid:
        if verify_email(recipient_email):
            email_not_valid = False
        else:
            recipient_email = input('That email was incorrect, please insert a correct one!')
    return recipient_email


def get_file_path_to_read(recipient_email: str) -> (bool, str):
    if path.isfile(f'mails/{recipient_email}.txt'):
        file_path = f'mails/{recipient_email}.txt'
        return True, file_path
    else:
        return False, 'file does not exist, you do not have any mail incoming'


def read_emails(file_path):
    file = open(file_path, 'r')
    line = file.readline()
    mails = []
    mail = []
    while line:
        line = line.strip().split('###')
        if line[0] == 'datetime_created':
            mail.append((line[0], line[1]))
            mails.append(mail)
            mail = []
        else:
            mail.append((line[0], line[1]))
        line = file.readline()
    file.close()
    return mails


def display_all_mails(mails):
    for mail in mails:
        print(f'\nMail incoming from: {mail[0][1]}')
        print(f'Mail subject: {mail[1][1]}')
        print(f'Mail text: {mail[2][1]}')
        print(f'Mail sent at date-time: {mail[3][1]}\n')


def sort_mails_sender(mails):
    sorted_mails = sorted(mails, key=lambda x: x[0][1])
    return sorted_mails


def sort_mails_subject(mails):
    sorted_mails = sorted(mails, key=lambda x: x[1][1])
    return sorted_mails


def sort_mails_date(mails):
    sorted_mails = sorted(mails, key=lambda x: x[3][1], reverse=True)
    return sorted_mails


def interact_with_mails(mails):
    quit_not_initiated: bool = False
    while not quit_not_initiated:
        user_input = input('What would you want to do with all your received emails? \n'
                           'To display them all write: "1"\n'
                           'To sort them by sender ascending, write: "2"\n'
                           'To sort them all by date descending, write: "3"\n'
                           'To sort them all by subject ascending, write: "4"\n'
                           'To exit the program, write: "5"\n')
        if user_input.isdigit():
            user_input_int = int(user_input)
            if 0 < user_input_int < 6:
                match user_input_int:
                    case 1:
                        display_all_mails(mails)
                    case 2:
                        mails = sort_mails_sender(mails)
                        display_all_mails(mails)
                    case 3:
                        mails = sort_mails_date(mails)
                        display_all_mails(mails)
                    case 4:
                        mails = sort_mails_subject(mails)
                        display_all_mails(mails)
                    case 5:
                        quit_not_initiated = True
            else:
                print('please insert a number from 1 to 5')
        else:
            print('please insert a number')


if __name__ == '__main__':
    recipient_email = 'marek@culak.sk'  # email_verification(input('What is your email?'))
    file_path = get_file_path_to_read(recipient_email)
    if file_path[0]:
        mails = read_emails(file_path[1])
        interact_with_mails(mails)
    else:
        print(file_path[1])
