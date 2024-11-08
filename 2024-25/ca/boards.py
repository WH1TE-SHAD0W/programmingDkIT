from typing import List
from post import Post
from user import User, Moderator

def boards_init() -> dict:
    Posts: dict = {
        'Moderator': [],
        'User': [],
        'Reader': [],
        'Subscriber': [],
    }
    return Posts

def seed_users() -> list[User | Moderator]:
    Users: list[User | Moderator] = [
        User(_username='Marek', _password='7PFxwtsd235'),
        User(_username='Michelle', _password='7PFxwtsd235'),
        User(_username='Marian', _password='5165dJOIsw'),
        Moderator(_username='Andrew', _password='685d3498ajHJ', _modded_groups=['User', 'Moderator']),
    ]
    return Users

def log_in(users, username, password) -> tuple[bool, (User | None)]:
    for user in users:
        if user.get_username() == username:
            if user.check_credentials(password):
                return True, user
    return False, None

def user_main_menu() -> str:
    return  (
        'Which of followings you want to do? Type following number to access: \n'
        '1 for displaying all available groups, \n'
        '2 for displaying all posts in a certain group, \n'
        '3 to add a new post \n'
        '4 to log out'
        )
def moderator_main_menu() -> str:
    return (
        'Which of followings you want to do? Type following number to access: \n'
        '1 for displaying all available groups, \n'
        '2 for displaying all posts in a certain group, \n'
        '3 to add a new post, \n'
        '4 to view all groups assigned to you, \n'
        '5 to add a group to you as a moderator'
        )

def print_groups(posts):
    print("Already created groups are: ")
    for group in posts:
        print(group, end=', ')
    print()

def create_post(user, posts):
    group = input('To which should be post added?')
    post = Post(
        author=user.get_username(),
        message=input('What is the post message?')
    )
    posts[group].appen(post)

def view_posts(group, posts):
    for post in posts[group]:
        print(post)

def view_mod_groups(user: Moderator):
    mod_groups = user.get_groups()
    for group in mod_groups:
        print(group)

def add_group_to_modded_groups(user: Moderator):
    group = input('What is the group you want to add there?')
    if group not in user.get_groups():
        if user.add_group(group):
            print('The group was added successfully')
        else:
            print('There was and error adding the group')

def app(posts, user):
    print(user)
    user_logged_in = True
    while user_logged_in:
        if isinstance(user, Moderator):
            match input(moderator_main_menu()):
                case '1':
                    print_groups(posts)
                case '2':
                    create_post(user, posts)
                case '3':
                    user_logged_in=False
        else:
            match input(user_main_menu()):
                case '1':
                    print_groups(posts)
                case '2':
                    create_post(user, posts)
                case '3':
                    create_post(user, posts)
                case '4':
                    view_mod_groups(user)
                case '5':
                    add_group_to_modded_groups(user)
                case '6':
                    user_logged_in=False






if __name__ == '__main__':
    posts = boards_init()
    users = seed_users()
    user_logged_in = False
    while not user_logged_in:
        session_controll = log_in(
            users=users,
            username=input('What is your username?'),
            password=input('What is your password?'),
        )
        if session_controll[0]:
            user_logged_in = True
            app(posts, session_controll[1])
