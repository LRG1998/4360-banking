from account import Account

def withdraw(acc, amount: float):
    acc.Balance -= amount

def verify(database, name:str,amount:float):
    for acc in database.accounts:
        if acc.Name == name:
            if acc.Balance>= amount:
                print("Amount verified")
                withdraw(acc, amount)
            else:
                print("verification failed")

def deposit(database, name:str, amount:float):
    for acc in database.accounts:
        if acc.Name == name:
            acc.Balance += float("%.2f" % amount)