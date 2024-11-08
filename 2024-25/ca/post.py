class Post:
    def __init__(self, author: str, message: str):
        self.author = author
        self.message = message

    def __str__(self):
        return f"Post with author: {self.author} and message '{self.message}"

    def __repr__(self):
        return f"Post['author':{self.author}, 'message':{self.message}]"

    def __format__(self, format_spec: str):
        match format_spec.lower():
            case "short":
                return f"Post named: {self.author}"
            case "complete":
                return f"Post written by {self.author} with the message: {self.message}"

    def __eq__(self, other):
        return (self.author == other.author) and (self.message == other.message)

    def __ne__(self, other):
        return not ((self.author == other.author) and (self.message == other.message))

