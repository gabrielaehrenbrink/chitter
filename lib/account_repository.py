from lib.account import Account


class AccountRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all books
    def all(self):
        rows = self._connection.execute('SELECT * from accounts')
        accounts = []
        for row in rows:
            item = Account(row["id"], row["username"], row["email"], row["user_password"])
            accounts.append(item)
        return accounts


    def create(self, account):
        rows = self._connection.execute('INSERT INTO accounts (username, email, user_password) VALUES (%s, %s, %s) RETURNING id', [account.username, account.email, account.user_password])
        account.id = rows[0]['id']
        return None


