from account import Account

def withdraw(database, name:str, amount: float):
    for acc in database.accounts:
        if acc.Name == name:
            if acc.Balance >= amount:
                acc.Balance -= amount
                print("Withdrawal complete!")
                print(acc.Name, " " ,acc.Balance)
            else:
                 print("Withdrawal failed!")

