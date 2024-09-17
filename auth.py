from account import Account
from accountDB import accounts


def valid(Username: str, password: str):
    for acc in accounts:
        if acc.Username == Username and acc.Password == password:
            return True
        else:
            return False
