from typing import LiteralString, List


class User:
    """Pre-defined class of a User.
    This class provides a basic structure with _username, _password attributes.

    Attributes:
        _username (str): The name of the user.
        _password (str): The _password of the user.
    """

    def __init__(self, _username: str, _password: str):
        """
        Initializes the User class.

        Args:
            _username (str)
            _password (str)

        Example:
            user = User("John", "_password")
        """
        self._username = _username
        password_validation = self.validate_password(_password)
        if password_validation[0]:
            self._password = _password
        else:
            print(password_validation[1])

    def validate_password(self, password: str):
        if len(password) < 7:
            return False, 'Password should be at least 8 character long.'
        lower = 0
        upper = 0
        number = 0
        for character in password:
            if character.islower():
                lower += 1
            elif character.isupper():
                upper += 1
            elif character.isdigit():
                number += 1
        if lower == 0:
            return False, 'Password should contain at least one lowercase character'
        elif upper == 0:
            return False, 'Password should contain at least one uppercase character'
        elif number == 0:
            return False, 'Password should contain at least one digit'
        else:
            return True, 'Password accepted'

    def check_credentials(self, password: str):
        if self._password == password:
            return True
        else:
            return False

    def change_password(self, old_password: str, new_password: str):
        if self.check_credentials(old_password) and self.validate_password(new_password):
            self._password = new_password
            return True
        else:
            return False

    def get_username(self):
        return self._username

    def __str__(self):
        """
            Returns a string of the User object in a user-readable format.

            Example:
                print(user)
                #User with name: John
        """
        return f"User with name: {self._username}"

    def __repr__(self):
        """
            Returns a string of the User object in a developer-usable format.

            Example:
                print(user.__repr__())
                #User['_username':John, '_password':_password]
        """
        return f"User['_username':{self._username}, #hashed '_password':{hash(self._password)}]"

    def __format__(self, format_spec: str):
        """
            Returns a string of the User object, based on the format provided.

            Example:
                print(user.__format__("simple"))
                #User named: John
        """
        match format_spec.lower():
            case "short":
                return f"User named: {self._username}"
            case "complete":
                return f"User's username is {self._username} and the hashed password is {hash(self._password)}"
            case _:
                return self.__str__()

    def __eq__(self, other):
        """
            Compares two User objects. Returns True if they are equal.

            Argument:
                other: User object to compare with.

            Example:
                other_user = User("David", "david@dan.com", "_password")
                print(user.__eq__(other_user))
                #False
        """
        return (self._username == other._username)

    def __ne__(self, other):
        """
            Compares two User objects. Returns True if they are not equal.

            Argument:
                other: User object to compare with.

            Example:
                print(user.__ne__(other_user))
                #True
        """
        return not (self._username == other._username)

    def __hash__(self):
        """
            Generates an ID as a string of the User object based on the user attributes.

            Example:
                print(user.__hash__())
                #-9223372036854775808
        """
        return hash(self._username)

class Moderator(User):
    def __init__(self, _username:str, _password:str, _modded_groups: list = ['Moderator']):
        super().__init__(_username, _password)
        self._modded_groups = _modded_groups

    def add_group(self, group: str):
        if group[0].isupper() and len(group) > 4:
            self._modded_groups.append(group)
            return True
        else:
            return False

    def get_groups(self):
        groups: List = []
        for group in self._modded_groups:
            groups.append(group)
        return groups

    def __str__(self):
        return f"Moderator with name: {self._username}"

    def __repr__(self):
        return f"Moderator['_username':{self._username}, #hashed '_password':{hash(self._password)}, 'modded_groups': {self._modded_groups}]"

    def __format__(self, format_spec: str):
        match format_spec.lower():
            case "short":
                return f"User named: {self._username}"
            case "complete":
                return f"User's username is {self._username}, the hashed password is {hash(self._password)} and moderators modded groups are: {self._modded_groups}"
            case _:
                return self.__str__()

    def __eq__(self, other):
        return self._username == other._username

    def __ne__(self, other):
        return not (self._username == other._username)

    def __hash__(self):
        return hash(self._username)