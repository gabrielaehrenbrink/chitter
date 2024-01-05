from lib.account_repository import AccountRepository
from lib.account import Account

def test_create(db_connection):
    db_connection.seed("seeds/posts.sql") 
    repository = AccountRepository(db_connection)
    account = Account(None, "mike10", "mike@yahoo.com", "Ilovegab123!")
    repository.create(account)
    assert account.id == 4
    
def test_get_all_records(db_connection): 
    db_connection.seed("seeds/posts.sql") 
    repository = AccountRepository(db_connection) 

    accounts = repository.all()
    assert accounts == [
        Account(1, 'gab123', 'gab@gmail.com', 'password123!'),
        Account(2, 'b0b', 'bob@hotmail.com', 'p123321%'),
        Account(3, 'user123', 'user123@gmail.com', 'word?35pass')
        ]
    


