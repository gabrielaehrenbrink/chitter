class Post:

    def __init__(self, id, post_content, account_username):
        self.id = id
        self.post_content = post_content
        self.account_username = account_username

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Post({self.id}, {self.post_content}, {self.account_username})"

