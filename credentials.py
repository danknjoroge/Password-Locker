from random import choice
from user import User

class Credentials:

    crededential_list = []
    def __init__(self, account, user_name, password):
        self.account = account
        self.user_name = user_name
        self.password = password

    def save_credentials(self):
        Credentials.crededential_list.append(self)

    def delete_credentials(self):
        Credentials.crededential_list.remove(self)

    def display_credentials(cls):
        return cls.crededential_list

    
    @classmethod
    def find_credentials(cls, account):
        for credential in cls.crededential_list:
            if credential.account == account:
                return True
        


    def credential_exists(cls, account):
        for credential in cls.crededential_list:
            if credential.account == account:
                return True
        return False



