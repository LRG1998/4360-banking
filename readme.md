# LoTek Bank
This is a python application that creates a fictional bank known as LoTek Bank


## Usage
To use, run the following command after navigating to the directory

```bash
python3 executable.py
```

The application will open a menu at startup where you can either log in, create an account, or quit the application.  

There will be 2 premade accounts
```
UserName George123
Password 12345

UserName Joshua246
Password JustLogMeIn
```

The accounts will have $100.00 and $1,000.00 respectively

If you create an account, you can choose how much money to initially deposit into your account. 

After logging into an account or creating an account, you will be brought to the account menu where you can withdraw money, deposit money, transfer money, close (delete your account), log out, or quit. 


Due to the accounts being stored in an array in memory, created accounts are no persistent and will be deleted after the program closes. 