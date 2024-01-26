from lib.account import Account


class AccountRepository:

    def __init__(self, connection):
        self._connection = connection


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
    
    def find_by_id(self, id):
        rows = self._connection.execute('SELECT * FROM accounts WHERE id = %s', [id])
        if rows: 
            row = rows[0]
            return Account(row["id"], row["username"], row["email"], row["user_password"])
        else: 
            return None
        
    def get_by_username(self, username):
        rows = self._connection.execute('SELECT * FROM accounts WHERE username = %s', [username])
        if rows: 
            row = rows[0]
            return Account(row["id"], row["username"], row["email"], row["user_password"])
        else: 
            return None

    def authenticate(self, username, user_password):
        account = self.get_by_username(username)
        if account and account.user_password == user_password:
            return account
        return None

