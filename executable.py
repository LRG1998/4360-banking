import index
import accountDB
import os
import transaction
import auth
from time import sleep

# Constant values
MAIN_MENU_OPTIONS = ["1", "2", "3"]
ACCOUNT_MENU_OPTIONS = ["1", "2", "3", "4", "5", "q"]

def clear_screen() -> None:
    """Clear the screen"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main() -> None:
    print("Welcome to LoTek Bank!" ," \n\n\n\n\n")
    print("1) Login to an account! " , "\n")
    print("2) Create an accounts!", "\n")
    print("3) Quit","\n")

    response = input("Please pick an option: ")
    handle_main_menu_response(response)

def handle_main_menu_response(response: str) -> None:
    """Handle the main menu response"""
    match response:
        case "1":
            clear_screen()
            index.login()
            clear_screen()
            account_menu()
        case "2":
            clear_screen()
            create_account()
        case "3" : 
            index.quit()
        case _:
            clear_screen()
            main()

def create_account() -> None:
    """Create a new account"""
    new_username = input("Enter a username: ")
    new_password = input("Enter your password: ")
    if not auth.valid(new_username, new_password):
        new_name = input("Enter your name: ")
        initial_balance = float(input("Enter the starter balance: "))
        index.accountdb.create(new_username, new_name, new_password, initial_balance)
        index.set_new_active()
        clear_screen()
        account_menu()
    else:
        clear_screen()
        main()

def account_menu() -> None:
    """Account menu"""
    print(index.get_active().Name, "             ", index.get_active().Balance)
    print("\n" * 10)
    print(" 1) Deposit \n 2) Withdraw \n 3) Transfer \n 4) Close (Delete Account) \n 5) Logout \n \n Q) Quit")

    account_menu_response = input("Please pick an option:  ")
    handle_account_menu_response(account_menu_response)

def handle_account_menu_response(response: str) -> None:
    """Handle the account menu response"""
    clear_screen()
    match response.lower():
        case "1":
            deposit_menu()
        case "2":
            withdraw_menu()
        case "3":
            transfer_menu()
        case "4":
            index.accountdb.accounts.pop(index.get_active())
        case "5":
            index.clear_active()
            main()
        case "q":
            index.quit()
        case _:
            account_menu()

def transfer_menu() -> None:
    """Transfer menu"""
    to_account = input("Who are you transferring to? ")
    amount = input("How much do you want to transfer? ")
    transaction.transfer(index.get_active(), index.accountdb.accounts[index.accountdb.fetch(to_account)], amount)
    clear_screen()
    account_menu()

def deposit_menu() -> None:
    """Deposit menu"""
    amount = input("Enter amount to deposit: ")
    transaction.deposit(index.get_active(), amount)
    clear_screen()
    account_menu()

def withdraw_menu() -> None:
    """Withdraw menu"""
    amount = input("How much do you want to withdraw? ")
    transaction.withdraw(index.get_active(), amount)
    clear_screen()
    account_menu()

if __name__ == "__main__":
    main()