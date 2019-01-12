"""Tests for the user endpoints"""

import unittest
import json

from app import create_app

class ValidationsBaseTest(unittest.TestCase):
    """
    Set up the user validation tests
    """

    def setUp(self):
        """
        lets declare the variables to use on the tests
        """
        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.signup_user= {"firstname":"Tony",
                             "lastname": "MIT",
                             "username":"blairt001",
                             "email":"blairt371.dev@gmail.com",
                             "password": "Blairman1234",
                             "confirm_password":"Blairman1234"}

        self.user_email1_invalid = {"firstname":"Lionel",
                             "lastname": "Messi",
                             "username":"limesi",
                             "email":"limesigmail.com",
                             "password": "Limesi1234",
                             "confirm_password":"Limesi1234"}

        self.user_email2_invalid = {"firstname":"Joshua",
                             "lastname": "Ariga",
                             "username":"arigajosh",
                             "email":"ariga@gmailcom",
                             "password": "Ariga123",
                             "confirm_password":"Ariga123"}

        self.user_password_length = {"firstname":"Codeman",
                             "lastname": "Pragmatic",
                             "username":"codeprag",
                             "email":"codeman@gmail.com",
                             "password": "Code",
                             "confirm_password":"Code"}

        self.user_password_alphabetic = {"firstname":"Codeman",
                             "lastname": "Pragmatic",
                             "username":"codeprag",
                             "email":"codeman@gmail.com",
                             "password": "20192019",
                             "confirm_password":"20192019"}

        self.user_password_capital = {"firstname":"Kenyan",
                             "lastname": "Man",
                             "username":"kenyaa",
                             "email":"kenyan@gmail.com",
                             "password": "blairt1234",
                             "confirm_password":"blair1234"}

        self.user_password_number = {"firstname":"Kenyan",
                             "lastname": "Man",
                             "username":"kenyaa",
                             "email":"kenyan@gmail.com",
                             "password": "Blairtony",
                             "confirm_password":"Blairtony"}

    #clean up the tests
    def tearDown(self):
        self.app.testing = False

#lets now test for user validations
class TestValidations(ValidationsBaseTest):

    #tests if email is already taken
    def test_if_email_is_already_taken(self):
        self.client.post("api/v1/auth/signup", data = json.dumps(self.signup_user), content_type = "application/json")
        response = self.client.post("api/v1/auth/signup", data = json.dumps(self.signup_user), content_type = "application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['error'],"Email is already taken!")

    #tests if user enters an invalid email
    def test_user_enter_an_invalid_email1(self):
        response = self.client.post("api/v1/auth/signup", data = json.dumps(self.user_email1_invalid), content_type = "application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['error'],"Email is Invalid")

    #tests if a user enters an invalid email
    def test_user_enter_an_invalid_email2(self):
        response = self.client.post("api/v1/auth/signup", data = json.dumps(self.user_email2_invalid), content_type = "application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['error'],"Email is Invalid")

    #tests if a user uses the correct password length
    def test_correct_user_pasword_length(self):
        response = self.client.post("api/v1/auth/signup", data = json.dumps(self.user_password_length), content_type = "application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['error'],"Password should not be less than 8 characters or exceed 20")

    #tests if a users password contain an alphabet
    def test_user_pasword_is_alphabets(self):
        response = self.client.post("api/v1/auth/signup", data = json.dumps(self.user_password_alphabetic), content_type = "application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['error'],"Password should contain a letter between a-z")

    #tests if a users password contains a capital letter
    def test_user_pasword_contains_capital(self):
        response = self.client.post("api/v1/auth/signup", data = json.dumps(self.user_password_capital), content_type = "application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['error'],"Password should contain a capital letter")

    #tests if a users password contains a number
    def test_user_pasword_number(self):
        response = self.client.post("api/v1/auth/signup", data = json.dumps(self.user_password_number), content_type = "application/json")
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['error'],"Password should contain a number(0-9)")
