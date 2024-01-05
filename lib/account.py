class Account:

    def __init__(self, id, username, email, user_password):
        self.id = id
        self.username = username
        self.email = email
        self.user_password = user_password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Account({self.id}, {self.username}, {self.email}, {self.user_password})"

