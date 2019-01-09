"""Tests for meetups records"""
#imports
import os
import unittest
import json
 
from app import create_app

class MeetupsBaseTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.post_meetup = {"topic":"Scrum",
                            "happenningOn":"14/02/2019",
                            "location":"Thika",
                            "images":["blair.png", "tony.png"],
                            "tags":["Tech", "Health"]
                           }
        self.post_meetup2 = {"topic":"Fullstack",
                             "happenningOn":"15/02/2019",
                             "location":"Nairobi",
                             "images":["west.png", "east.png"],
                             "tags":["Tech", "Health"]
                            }
        self.meetups = []


class TestMeetupsRecords(MeetupsBaseTest):
    """
    We test for all the meetup endpoints
    """

    def test_admin_can_create_a_meetup(self):

        """ Test for admin creating a meetup"""

        response = self.client.post("api/v1/meetups",data = json.dumps(self.post_meetup), content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["data"], [{"location": "Thika","happenningOn": "14/02/2019","images": ["blair.png","tony.png"],"tags": ["Tech","Health"],"topic": "Scrum"}])
