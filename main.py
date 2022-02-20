#!/usr/bin/env python3.9



from user import User
from credentials import Credentials

def create_users(name, passw):
    newUser = User(name, passw)
    return newUser

def save_users(user):
    user.save_user()

def existing_user_check(name):
    return User.user_exist(name)

def login_user(name, password):
    login= User.login(name, password)
    if login != False:
        return User.login(name, password)

def display_users():
    return User.display_user()

def delete_user(user):
    return user.delete_user()

def create_credentials(accountName,accountUsername,accountPassword):
    newCredential = Credentials(accountName,accountUsername,accountPassword)
    return newCredential

def save_credentials(credentials):
    credentials.save_credential()

def delete_credentials(credentials):
    credentials.delete_credentials()

def display_credentials():
    return Credentials.display_credentials()

def generate_password(accountName):
    password = Credentials.generate_password()
    return password

def main():
    print("""Welcome to password locker! \n
    What is your name?
    """)
    name = input()
    print(f'Hello {name}, enjoy as you explore our applications!')

    while True:
        print("Use the following codes \n cr: create user account \n log: login to your account \n dis: display names of the user \n ex: exit from the account")
        code = input().lower()
        
        if code == 'cr':
            '''creating user account'''

            print("New User Account")
            print("-" *10)

            print('Input Username')
            username = input()

            print('Input Password')
            password = input()

            save_users(create_users(username, password))
            print(f'Hi {username} account Successfully created')

        elif code == 'log':
            print('Enter you information to login into your account')
            print('Please enter your username')
            username = input()
            print('Enter your password')
            password = input()

            if login_user(username, password) == None:
                print('If you have an account try again, if not create an account')
            else:
                login_user(username, password)
                print(f'Welcome {username} Select the service you want below')
                while True:
                    print('Select shortcode related to servce you want \n ca: add a credential \n dc: display credentials \n gc: generate password for account \n ex: back to main menu')
                    code = input().lower()
                    if code == 'ca':
                        print('Create a new Account Credential')
                        print('-'*10)

                        print('Input account name:')
                        accountName = input()

                        print('Input account Username:')
                        username = input()

                        print('Input account Password:')
                        password = input()

                        save_credentials(create_credentials(accountName, username, password))
                        print(f'Successfully created credentials for {accountName} account')

                    elif code == 'dc':
                        if display_credentials():
                            print(f' Account Credential Details')
                            print('-'*10)

                            for credential in display_credentials():
                                print(f'Account:...{credential.account}')

                                print(f'Username:...{credential.user_name}')
                                print(f'Password:...{credential.password}')
                                print('-'*10)
                        
                        else:
                            print('You have no existing credentials')

                    elif code == 'gc':
                        '''creating account with generated password'''
                        print('Account with generated password')
                        print('-'*10)

                        print('Input account name')
                        accountName= input()
                        print('Input Username of account')
                        username= input()

                        '''save account details credentials withgenerated password'''
                        save_credentials(Credentials(accountName, username,(generate_password(accountName)) ))
                        print(f'Password for {accountName} have been generated')

                    elif code == 'ex':
                        print(f'Thank you {username} for using our application')
                        break

                    else:
                        print(f'{code} is not available in our options. Please confirm the options and try again!')
                        



        






if __name__ == "__main__":
    main()