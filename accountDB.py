from account import Account

accounts = []
activeAccount = None
def create(Username : str, name: str, password: str, balance: float):
    accounts.append(Account())
    accounts[-1].Name = name
    accounts[-1].Username = Username
    accounts[-1].Password = password
    accounts[-1].Locked = False
    accounts[-1].Balance = balance

def lock(id: int):
    if 0 <= id < len(accounts):
        accounts[id].Locked = not accounts[id].Locked
    else:
        raise IndexError("Invalid account ID")

def fetch(accName:str):
    for acc in accounts:
        if acc.Username == accName:
            return accounts.index(acc)


def accountGrab(*args):
    for acc in accounts:
        if acc.Username == args[0]:
            return acc
            
