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
                             "password": "blairman1234",
                             "confirm_password":"blairman1234"}

        self.signup_user2 = {"firstname":"Lionel",
                             "lastname": "Messi",
                             "username":"limesi",
                             "email":"limesi@gmail.com",
                             "password": "limesi123",
                             "confirm_password":"limesi123"}

        self.signup_user3 = {"firstname":"Joshua",
                             "lastname": "Ariga",
                             "username":"arigajosh",
                             "email":"ariga@.com",
                             "password": "ariga123",
                             "confirm_password":"ariga123"}

        self.signup_user4 = {"firstname":"Codeman",
                             "lastname": "Pragmatic",
                             "username":"codeprag",
                             "email":"codeman@gmail.com",
                             "password": "code123",
                             "confirm_password":"code123"}

    #clean up the tests
    def tearDown(self):
        self.app.testing = False

