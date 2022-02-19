

# from credentials import Credentials

class User:
    '''
    A user class that will be used to generate class instances user
    '''

    user_list = []

    def __init__(self, username, password):
        '''
         __init__ method to define properties of user object
        '''
        self.username = username
        self.password = password


    def save_user(self):
        '''Method that saves user object'''
        User.user_list.append(self)


    @classmethod
    def display_user(cls):
        '''Method that returns user list'''
        return cls.user_list


    def delete_user(self):
        User.user_list.remove(self)

    def log_in(cls,username,password):
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return User.user_list()
            return False

    @classmethod
    def user_exist(cls,username,password):
        for user in cls.user_list:
            if user.username == username:
                return True
        return False


    



    





