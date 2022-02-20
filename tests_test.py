import unittest
from credentials import Credentials
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Daniel", 'Dan1234')

    def tearDown(self):

        User.user_list = []


    def test_init(self):
        self.assertEqual(self.new_user.username, 'Daniel')
        self.assertEqual(self.new_user.password, 'Dan1234')

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_delete_user(self):
        self.new_user.save_user()
        newUser = User('Mary','Mary1234')
        newUser.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_display_users(self):
        self.assertEqual(User.display_user(), User.user_list)


    
    def test_login_user(self):
        self.new_user.save_user()
        newUser = User('Mary','Mary1234')
        newUser.save_user()

        user = User.login('Mary','Mary1234')
        self.assertEqual(user, User.user_list)


    def test_user_exists(self):
        self.new_user.save_user()
        newUser = User('Mary','Mary1234')
        newUser.save_user()

        useer = User.user_exist('Mary')
        self.assertTrue(useer)

    

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credentials('twitter','Daniel','Dan123')

    def tearDown(self):
        Credentials.crededential_list= []

    def test_init(self):
        self.assertEqual(self.new_credentials.account, 'twitter')
        self.assertEqual(self.new_credentials.user_name, 'Daniel')
        self.assertEqual(self.new_credentials.password, 'Dan123')

    def test_save_credentials(self):
        self.new_credentials.save_credential()
        self.assertEqual(len(Credentials.crededential_list),1)

    def test_save_multiple_credentials(self):
        self.new_credentials.save_credential()
        newCredential = Credentials('twitter','Joy','Joy123')
        newCredential.save_credential()

        self.assertEqual(len(Credentials.crededential_list),2)

    def test_delete_credentials(self):
        self.new_credentials.save_credential()
        newCredential = Credentials('twitter','Joy','Joy123')
        newCredential.save_credential()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.crededential_list),1)

    def test_display_credentials(self):
        self.assertEqual(Credentials.display_credentials(), Credentials.crededential_list)

    # def test_find_credentials(self):
    #     self.new_credentials.save_credential()
    #     newCredential = Credentials('twitter','Joy','Joy123')
    #     newCredential.save_credential()

    #     existCred = Credentials.find_credentials('joy')
    #     self.assertEqual(existCred.account, newCredential.account)  


    def test_credentials_exists(self):
        self.new_credentials.save_credential()
        newCredential = Credentials('twitter','Joy','Joy123')
        newCredential.save_credential()


        existCred = Credentials.credential_exists('twitter')
        self.assertTrue(existCred)

    def test_generate_password(self):
        genPass = self.new_credentials.generate_password()
        self.assertEqual(len(genPass), 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)