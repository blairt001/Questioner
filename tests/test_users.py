"""Tests for the user endpoints"""

import unittest
import json

from app import create_app

class UserBaseTest(unittest.TestCase):
    """
    Set up the user tests
    """

    def setUp(self):
        """
        lets declare the variables to use on the tests
        """
        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.signup_user1 = {"firstname":"Tony",
                             "lastname": "Blair",
                             "username":"blairt001",
                             "email":"blairt371.dev@gmail.com",
                             "password": "Blairman1234",
                             "confirm_password":"Blairman1234"}

        self.signup_user2 = {"firstname":"Lionel",
                             "lastname": "Messi",
                             "username":"limesi",
                             "email":"limesi@gmail.com",
                             "password": "Limesi1234",
                             "confirm_password":"Limesi123"}

        self.signup_user3 = {"firstname":"Joshua",
                             "lastname": "Ariga",
                             "username":"arigajosh",
                             "email":"ariga@.com",
                             "password": "Ariga123",
                             "confirm_password":"Ariga123"}

        self.signup_user4 = {"firstname":"Codeman",
                             "lastname": "Pragmatic",
                             "username":"codeprag",
                             "email":"codeman@gmail.com",
                             "password": "Code123",
                             "confirm_password":"Code123"}

        self.signup_user5 = {"firstname":"Kenyan",
                             "lastname": "Man",
                             "username":"kenyaa",
                             "email":"kenyan@gmail.com",
                             "password": "@Mitcoder1",
                             "confirm_password":"@Mitcoder1"}

        self.login_user1 = {"username":"blairt001",
                            "password":"Blairman1234"}

        self.login_user2 = {"username":"limesi",
                            "password":"Limesi1234"}

        self.login_user3 = {"username":"kenyaa",
                            "password":"@Mitcoder1"}

    #clean up the tests
    def tearDown(self):
        self.app.testing = False

#testing for the users endpoints
class TestUsersEndpoints(UserBaseTest):
   
    def test_user_can_sign_up(self):
        """
        Tests to confirm a user signup successfully
        """
        response = self.client.post("api/v1/auth/signup", data = json.dumps(self.signup_user1), content_type = "application/json")
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['data'], 'User Registered Successfully!')

    #tests that user sign-up passwords match
    def test_user_enter_unmatching_passwords(self):
       
        response = self.client.post("api/v1/auth/signup", data = json.dumps(self.signup_user2), content_type = "application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["error"], "Your passwords don't match!")

    #tests that a user can issue a correct pasword and login
    def test_user_can_login_with_correct_password(self):
        self.client.post("api/v1/auth/signup", data = json.dumps(self.signup_user1), content_type = "application/json")
        response = self.client.post("api/v1/auth/login", data = json.dumps(self.login_user1), content_type = "application/json")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertTrue(result['token'])
        self.assertEqual(result["message"], "You have Logged in Successfully")

    #User logs in with wrong password or is unregistered user
    def test_wrong_password_and_unregistered_user_no_login(self):
        response = self.client.post("api/v1/auth/login", data = json.dumps(self.login_user2), content_type = "application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["data"], "Please Register First to Login")

   