#!/usr/bin/env python3.9

from user import User
from credentials import Credentials

def create_users(name, passw):
    '''Function to create user account'''
    newUser = User(name, passw)
    return newUser

def save_users(user):
    '''Function to save user account'''
    user.save_user()

def existing_user_check(name):
    '''Function checking if user account exists'''
    return User.user_exist(name)

def login_user(name, password):
    '''function that allows user to login to the account'''
    login= User.login(name, password)
    if login != False:
        return User.login(name, password)

def display_users():
    '''function to display users present'''
    return User.display_user()

def delete_user(user):
    '''function to delete user'''
    return user.delete_user()

def create_credentials(accountName,accountUsername,accountPassword):
    '''Function to create a new credentials'''
    newCredential = Credentials(accountName,accountUsername,accountPassword)
    return newCredential

def save_credentials(credentials):
    '''function to save credentials'''
    credentials.save_credential()

def delete_credential(credentials):
    '''function to delete credentials'''
    credentials.delete_credentials()

def display_credentials():
    '''function to display all present credentials information'''
    return Credentials.display_credentials()

def generate_password(accountName):
    '''function to generate a new password'''
    password = Credentials.generate_password()
    return password

def search_account(account):
    '''function to search an account present'''
    return Credentials.find_credentials()

def main():
    '''
    function to run the password locker account
    '''
    print("""Welcome to password locker! \n
    What is your name?
    """)
    name = input()
    print(f'Hello {name}, enjoy as you explore our applications!')

    while True:
        '''
        Loop that will control running of the application
        '''
        print("Use the following codes \n cr: create user account \n log: login to your account \n ex: exit from the account")
        code = input().lower()
        
        if code == 'cr':
            '''
            creating user account
            '''

            print("New User Account")
            print("-" *10)

            print('Input Username')
            username = input()

            print('Input Password')
            password = input()

            save_users(create_users(username, password))
            print(f'Hi {username} account Successfully created')

        elif code == 'log':
            '''
            logging in into the user account
            '''
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
                    print('Select shortcode related to servce you want: \n ca: Add a account credential with typed password  \n dc: Display Credentials Details present \n gc: Create account with generated password\n del: Delete Credentials not in use \n ex: back to main menu')
                    code = input().lower()
                    if code == 'ca':
                        '''
                        Create a new credential
                        '''
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
                        '''
                        Display credentials
                        '''
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
                        '''
                        creating credential account with generated password
                        '''
                        print('Account with generated password')
                        print('-'*10)

                        print('Input account name')
                        accountName= input()
                        print('Input Username of account')
                        username= input()

                        '''save account details credentials withgenerated password'''
                        save_credentials(Credentials(accountName, username,(generate_password(accountName)) ))
                        print(f'Password for {accountName} have been generated')

                    elif code == 'del':
                        '''
                        Delete an existing credential entry
                        '''
                        print('Enter account name of credentials to delete')
                        accountName = input().lower()
                        if search_account(accountName):
                            search = search_account(accountName)
                            print('-'*10)

                            search.delete_credential()

                            print(f'{accountName} credential details deleted')
                        else:
                            print(f'Account credentials doesn\'t exist')



                    elif code == 'ex':
                        print(f'Thank you {username} for using our application')
                        break

                    else:
                        print(f'{code} is not available in our options. Please confirm the options and try again!')
                        
        elif code == 'ex':
            print('Thank you for visiting our site')
            break
        else:
            print('Please check the code clearly and try again')


if __name__ == "__main__":
    main()