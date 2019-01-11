"""Tests for meetups records"""
#imports
import os
import unittest
import json

from app import create_app

#Our meetup base test with the setup function for initializing the tests
class MeetupsBaseTest(unittest.TestCase):

    def setUp(self):
        APP_ENV = os.getenv("TESTING_ENV")
        self.app = create_app(APP_ENV)
        self.client = self.app.test_client()

        self.post_meetup = {"topic":"Scrum",
                            "happenningOn":"14/02/2019",
                            "location":"Thika",
                            "images":["blair.png", "tony.png", "david.png"],
                            "tags":["Tech", "Health"]
                           }
        self.rsvp_response1 = [{"Attending": "yes",
                                "meetup": 1,
                                "topic": "Scrum"}]

class TestMeetupsRecords(MeetupsBaseTest):
    """
    We test for all the meetup endpoints
    """

    def test_admin_can_create_a_meetup(self):

        """ Test for admin creating a meetup"""

        response = self.client.post("api/v1/admin/MeetupModel",data = json.dumps(self.post_meetup), content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["data"], [{"location": "Thika","happenningOn": "14/02/2019","tags": ["Tech","Health"],"topic": "Scrum"}])
