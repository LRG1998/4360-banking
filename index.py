from account import Account
import accountDB
from transaction import *
import auth
import security
import os

accountdb = accountDB


accountdb.create("George123", "George", "12345", 100.00)
accountdb.create("Joshua246", "Joshua", "JustLogMeIn", 1000.00)

   

def create():
    loginName = input("Enter new username:  ")
    if loginName == None:
        os.system('cls')
        create()
    password = input("Enter password:  ")
    if auth.valid(loginName, password):
        name = input("Enter your name:  ")
        balance = input("Enter balance:  ")
        accountdb.create(loginName, name, password, int(balance))
        
    else:
       raise("Account already exists.")



def login():
    loginName = input("Enter username...  ")
    password = input("Enter Password...  ")
    if auth.valid(loginName, password):
        accountdb.activeAccount = accountdb.accountGrab(loginName)
    else:
        if security.loginAttempts >=3:
            accountdb.lock(accountdb.accounts.index(accountdb.fetch(loginName)))
        


def close():
    verifyName = input("Enter username to verify:  ")
    verifyPassword = input("Enter password to verify:  ")
    if auth.valid(verifyName, verifyPassword):
        for acc in accountdb.accounts:
            if acc.userName == verifyName and acc.Password == verifyPassword:
                accountdb.accounts.pop(accountdb.accounts.index(acc))
            else:
                pass

def getActive():
    return accountdb.activeAccount

def clearActive():
    accountdb.activeAccount = None

def setNewActive():
    accountdb.activeAccount = accountdb.accounts[-1]


def quit():
    pass
   