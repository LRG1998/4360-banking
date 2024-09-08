from account import Account

accounts = []
activeAccount = None
def create(username : str, name: str, password: str, balance: float):
    accounts.append(Account())
    accounts[-1].Name = name
    accounts[-1].userName = username
    accounts[-1].Password = password
    accounts[-1].Locked = False
    accounts[-1].Balance = balance


def lock(id: int):
    accounts[id].Locked = not Locked

def fetch(accName:str):
    for acc in accounts:
        if acc.userName == accName:
            return accounts.index(acc)
            
