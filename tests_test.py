import pyperclip
import unittest
from credentials import Credentials
from user import User

class TestUser(unittest.TestCase):
    '''
    User test class definingf tests for user class behavior
    '''

    def setUp(self):
        '''
        Set up method to run before each test case starts running
        '''
        self.new_user = User("Daniel", 'Dan1234')

    def tearDown(self):
        '''
        teardown method cleans up list after each test case ends
        '''

        User.user_list = []


    def test_init(self):
        '''method to test if objects are initialized properly'''
        self.assertEqual(self.new_user.username, 'Daniel')
        self.assertEqual(self.new_user.password, 'Dan1234')

    def test_save_user(self):
        '''test case for checking if new user are saved to user_list'''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_delete_user(self):
        '''test case to test if we remove a user from the one present in the list'''
        self.new_user.save_user()
        newUser = User('Mary','Mary1234')
        newUser.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_display_users(self):
        '''test case testing if we can display all users in the list'''
        self.assertEqual(User.display_user(), User.user_list)


    
    def test_login_user(self):
        '''test case to check if user can login with their account credentials'''
        self.new_user.save_user()
        newUser = User('Mary','Mary1234')
        newUser.save_user()

        user = User.login('Mary','Mary1234')
        self.assertEqual(user, User.user_list)


    def test_user_exists(self):
        '''test case of checking whether a user is present'''
        self.new_user.save_user()
        newUser = User('Mary','Mary1234')
        newUser.save_user()

        useer = User.user_exist('Mary')
        self.assertTrue(useer)

    

class TestCredentials(unittest.TestCase):
    '''Test class for credentials'''

    def setUp(self):
        '''method to run before a test starts running'''
        self.new_credentials = Credentials('twitter','Daniel','Dan123')

    def tearDown(self):
        '''method to cleanup list before another test is done'''
        Credentials.crededential_list= []

    def test_init(self):
        '''test case to test if object is properly initialised'''
        self.assertEqual(self.new_credentials.account, 'twitter')
        self.assertEqual(self.new_credentials.user_name, 'Daniel')
        self.assertEqual(self.new_credentials.password, 'Dan123')

    def test_save_credentials(self):
        '''test case to check if credentials are added into credential list'''
        self.new_credentials.save_credential()
        self.assertEqual(len(Credentials.crededential_list),1)

    def test_save_multiple_credentials(self):
        '''test case to check if multiple entries can be added into the list'''
        self.new_credentials.save_credential()
        newCredential = Credentials('twitter','Joy','Joy123')
        newCredential.save_credential()

        self.assertEqual(len(Credentials.crededential_list),2)

    def test_delete_credentials(self):
        '''test case to check if we can remove a credential entry from the list'''
        self.new_credentials.save_credential()
        newCredential = Credentials('twitter','Joy','Joy123')
        newCredential.save_credential()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.crededential_list),1)

    def test_display_credentials(self):
        '''a test case to check if we can output all credentials present and their related account'''
        self.assertEqual(Credentials.display_credentials(), Credentials.crededential_list)

    # def test_find_credentials(self):
    #     self.new_credentials.save_credential()
    #     newCredential = Credentials('twitter','Joy','Joy123')
    #     newCredential.save_credential()

    #     existCred = Credentials.find_credentials('Daniel')
    #     self.assertEqual(existCred.user_name, newCredential.account)  


    def test_credentials_exists(self):
        '''test case to test if specified credentials exist'''
        self.new_credentials.save_credential()
        newCredential = Credentials('twitter','Joy','Joy123')
        newCredential.save_credential()


        existCred = Credentials.credential_exists('twitter')
        self.assertTrue(existCred)

    def test_generate_password(self):
        '''test case test whether we can generate a random password'''
        genPass = self.new_credentials.generate_password()
        self.assertEqual(len(genPass), 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)