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
        print("Use the following shortcodes cu: create user account \n log: login to your account \n dis: display names of the user \n ex: exit from the account")
        shortcodes = input().lower

        if shortcodes == 'cu' :
            '''creating user account'''
            print("New User Account")
            print('_'*11)

            print('Input Username')
            username = input()

            print('Input Password')
            password = input()

            save_users(create_users(username, password))
            print(f'Hi {username} account Successfully created')
        






if __name__ == "__main__":
    main()