from account import Account
import accountDB
from transaction import *
import auth
import security
import os
import sys
accountdb = accountDB


accountdb.create("George123", "George", "12345", 100.00)
accountdb.create("Joshua246", "Joshua", "JustLogMeIn", 1000.00)

   

def create():
    loginName = input("Enter new Username:  ")
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

        

    loginName = input("Enter Username...  ")
    password = input("Enter Password...  ")
    if security.loginAttempts >= 3:
        try:
            accountdb.lock(accountdb.fetch(loginName))
            print("This account is now Locked because of excessive login attempts")
        except Exception as e:
            print("This account doesn't exist")
            quit()

    if auth.valid(loginName, password):
        accountdb.activeAccount = accountdb.accountGrab(loginName)
        return
    else:
        print("Invalid username or password. Try again.")
        security.loginAttempts += 1
        login()
    


def close():
    verifyName = input("Enter Username to verify:  ")
    verifyPassword = input("Enter password to verify:  ")
    if auth.valid(verifyName, verifyPassword):
        for acc in accountdb.accounts:
            if acc.Username == verifyName and acc.Password == verifyPassword:
                accountdb.accounts.pop(accountdb.accounts.index(acc))
                accountdb.activeAccount = None
                return
            else:
                pass
    else:
        print("Invalid username or password.")

def getActive():
    return accountdb.activeAccount

def clearActive():
    accountdb.activeAccount = None

def setNewActive():
    accountdb.activeAccount = accountdb.accounts[-1]


def quit():
    sys.exit()
   