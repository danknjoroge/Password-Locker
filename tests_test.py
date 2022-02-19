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




if __name__ == '__main__':
    unittest.main(verbosity=2)