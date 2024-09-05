from account import Account
import accountDB
from transaction import *

loggedIn = False

accountdb = accountDB
accountdb.create("George", "12345", 1000.00)
withdraw(accountdb,"George", 100.00)

def main():    
    if loggedIn == False:
        login()

def login():
    loginName = input("Enter username...")
    password = input("Enter Password...")

