from account import Account
from accountDB import accounts


def valid(username: str, password: str):
    for acc in accounts:
        if acc.userName == username and acc.Password == password:
            return True
        else:
            return False
