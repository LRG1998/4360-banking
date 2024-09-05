from account import Account
from transaction import *

accounts = []

def create(name: str, password: str, balance: float):
    accounts.append(Account())
    accounts[-1].Name = name
    accounts[-1].Password = password
    accounts[-1].Locked = False
    accounts[-1].Balance = balance


def lock(name: str):
    for acc in accounts:
        if acc.Name == name:
            acc.Locked = True
    pass
