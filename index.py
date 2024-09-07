from account import Account
import accountDB
from transaction import *

loggedIn = False

accountdb = accountDB


def main():    
    if loggedIn == False:
        login()

def login():
    loginName = input("Enter username...")
    password = input("Enter Password...")

