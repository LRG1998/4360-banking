from account import Account
from security import transferAttempts


def verify(account: Account,amount:float):
    if database[ID].Balance > amount:
        return True
    else:
        return False

def withdraw(account:Account, amount:float):
    if account.Locked == False:
        if verify(account, amount):
            account.Balance -= amount
        else:
            print("Unable to verify amount")
            if transferAttempts < 3:
                transferAttempts += 1
            else:
                account.Locked = True


def deposit(account: Account, amount:float):
    database[ID].balance += float(amount % "%0.2f")

