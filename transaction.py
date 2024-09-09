from account import Account
from security import transferAttempts


def verify(account: Account,amount:float):
    if account.Balance > amount:
        return True
    else:
        return False

def withdraw(account:Account, amount:str):
    if account.Locked == False:
        if verify(account, float(amount)):
            account.Balance -= float(amount)
        else:
            print("Unable to verify amount")
            if transferAttempts < 3:
                transferAttempts += 1
            else:
                account.Locked = True


def deposit(account: Account, amount:str):
    account.Balance += float(amount)

def transfer(fromAcc: Account, toAcc: Account, amount:str):
    withdraw(fromAcc, amount)
    deposit(toAcc, amount)

