import pyperclip
from random import choice
import string
from user import User

class Credentials:

    crededential_list = []
    def __init__(self, account, user_name, password):

        '''__init__ method to define properties of user object'''
        
        self.account = account
        self.user_name = user_name
        self.password = password

    def save_credential(self):
        '''method to add credentials in the list'''
        Credentials.crededential_list.append(self)

    def delete_credentials(self):
        '''method to delete user credentials from the list'''
        Credentials.crededential_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''method to display all user credentials present'''
        return cls.crededential_list

    
    @classmethod
    def find_credentials(cls, account):
        '''method to find credentials by seraching by account name'''
        for credential in cls.crededential_list:
            if credential.account == account:
                return True

        return False
        

    @classmethod
    def credential_exists(cls, account):
        '''method to check if a credential for a specific account exists'''
        for credential in cls.crededential_list:
            if credential.account == account:
                return True
        return False


    @classmethod
    def generate_password(cls):
        '''method to generate a random password'''
        stringSize =10

        passCombination = string.ascii_lowercase + string.ascii_uppercase + string.digits
        generatedPassword = ''.join(choice(passCombination) for size in range(stringSize))
        return generatedPassword

    @classmethod
    def copy_password(cls, account):
        '''method that allow copying of password in clipboard '''
        copiedPassword = Credentials.find_credentials(account)
        pyperclip.copy(copiedPassword.password)