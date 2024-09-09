import index
import accountDB
import os
import transaction
import auth
from time import sleep

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    print("Welcome to LoTek Bank!" ," \n\n\n\n\n")
    print("1) Login to an account! " , "\n")
    print("2) Create an accounts!", "\n")
    print("3) Quit","\n")

    response = input("Please pick an option: ")
    mainHandle(response)

def mainHandle(response):
    match response:
        case "1":
            clear()
            index.login()
            clear()
            accountMenu()
        case "2":
            clear()
            createMenu()
        case "3" : 
            index.quit()
        case _:
            clear()
            main()

def createMenu():
    newUName = input("Enter a username: ")
    newPassword = input("Enter your password: ")
    if not auth.valid(newUName, newPassword):
        newName = input("Enter your name: ")
        initBalance = float(input("Enter the starter balance: "))
        index.accountdb.create(newUName,newName,newPassword,initBalance)
        index.setNewActive()
        clear()
        accountMenu()
    else:
        clear()
        main()

def accountMenu():
    print(index.getActive().Name, "             ", index.getActive().Balance)
    print("\n" * 10)
    print(" 1) Deposit \n 2) Withdraw \n 3) Transfer \n 4) Close (Delete Account) \n 5) Logout \n \n Q) Quit")

    accResponse = input("Please pick an option:  ")
    accountHandle(accResponse)

def accountHandle(response):
    match response.lower():
        case "1":
            clear()
            depMenu()
            pass
        case "2":
            clear()
            withdrawMenu()
            pass
        case "3":
            
            pass
        case "4":
            index.accountdb.accounts.pop(index.getActive())
            pass
        case "5":
            index.clearActive()
            clear()
            main()
            pass
        case "q":
            index.quit()
            pass
        case _:
            clear()
            accountMenu()
            pass


def transferMenu():
    toAcc = input("Who are you transferring to?")



def depMenu():
    amount = input("Enter amount to deposit: ")
    transaction.deposit(index.getActive(),amount)
    clear()
    accountMenu()

def withdrawMenu():
    amount = input("How much do you want to withdraw? ")
    transaction.withdraw(index.getActive(), amount)
    clear()
    accountMenu()

if __name__ == "__main__":
    main()