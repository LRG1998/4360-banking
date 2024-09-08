import index
import accountDB
import os


def main():
    print("Welcome to LoTek Bank!" ," \n\n\n\n\n")
    print("1) Login to an account! " , "\n")
    print("2) Create an accounts!", "\n")
    print("3) Quit","\n")

    response = input("Please pick an option: ")
    mainHandle(response)

def mainHandle(response):
    match response:
        case "3" : 
            index.quit()
        case _:
            clear = lambda: os.system("cls")
            clear()
            main()





if __name__ == "__main__":
    main()