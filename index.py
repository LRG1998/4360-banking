from account import Account
import accountDB
from transaction import *

loggedIn = False

accountdb = accountDB
accountdb.create("George", "12345", 1000.00)
deposit(accountdb, "George", 100.00)
accountdb.lock("George")
print(accountdb.accounts[-1].Locked)

accountdb.lock("George")
print(accountdb.accounts[-1].Locked)


def main():    
    if loggedIn == False:
        login()

def login():
    loginName = input("Enter username...")
    password = input("Enter Password...")

