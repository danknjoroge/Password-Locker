import unittest
# from credentials import Credentials
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





if __name__ == '__main__':
    unittest.main(verbosity=2)