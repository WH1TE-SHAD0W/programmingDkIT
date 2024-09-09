from datetime import datetime
from exercise_1 import verify_email
from os import path


def get_email_to_send(sender_email):
    email_not_valid: bool = True
    while email_not_valid:
        if verify_email(sender_email):
            email_not_valid = False
        else:
            sender_email = input('That email was incorrect, please insert a correct one!')

    email_not_valid: bool = True
    while email_not_valid:
        recipient_email = input('What is the recipient email?')
        if verify_email(recipient_email):
            email_not_valid = False

    subject = input('What is the mail subject?')
    text = input('What is the email body text?')
    return sender_email, subject, text, recipient_email


def send_email(mail_attributes: tuple, file):
    storage_mail_content = []
    content_types = ('sender_mail', 'subject', 'text')
    for content_type, content in zip(content_types, mail_attributes):
        line = f'{content_type + '###' + content + '\n'}'
        storage_mail_content.append(line)
    time = datetime.now()
    storage_mail_content.append(f'{'datetime_created' + '###' + str(time) + '\n'}')
    file.writelines(storage_mail_content)
    file.close()


def get_file(recipient_email):
    if path.isfile(f'mails/{recipient_email}.txt'):
        file = open(f'mails/{recipient_email}.txt', 'a')
        return file
    else:
        file = open(f'mails/{recipient_email}.txt', 'w')
        return file


if __name__ == '__main__':
    sender_email = input('What is your email?')
    email = get_email_to_send(sender_email)
    storage_file = get_file(email[3])
    send_email(email, storage_file)
