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

        self.post_meetup1 = {"topic":"Scrum",
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

        self.meetups = [{"created_at": "Wed, 09 Jan 2019 02:30:10 GMT",
                         "id": 1,
                         "images": ["blair.png",
                                    "tony.png"],
                         "location": "Thika",
                         "happenningOn": "14/02/2019",
                         "tags": ["Tech",
                                  "Health"],
                         "topic": "Scrum"},
                        {"created_at": "Wed, 09 Jan 2019 02:30:54 GMT",
                         "id": 2,
                         "images": ["west.png",
                                    "east.png"],
                         "location": "Nairobi",
                         "happenningOn": "15/02/2019",
                         "tags": ["Tech", "Health"],
                         "topic": "Fullstack"
                        }]



class TestMeetupsRecords(MeetupsBaseTest):
    """
    We test for all the meetup endpoints
    """

    def test_admin_can_create_a_meetup(self):

        """ Test for admin creating a meetup"""

        response = self.client.post("api/v1/meetups",data = json.dumps(self.post_meetup1), content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["data"], [{"location": "Thika","happenningOn": "14/02/2019","images": ["blair.png","tony.png"],"tags": ["Tech","Health"],"topic": "Scrum"}])

    def test_user_get_specific_meetup_record(self):
        """
        Test user can get specific meetup record using the meetup id
        """
        self.client.post("api/v1/meetups", data = json.dumps(self.post_meetup1), content_type = "application/json")
        self.client.post("api/v1/meetups", data = json.dumps(self.post_meetup2),  content_type = "application/json")

        response = self.client.get("api/v1/meetups/1", content_type = "application/json")
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['data'], [{"id": 1,
                                           "location": "Thika",
                                           "meetup_date": "14/02/2019",
                                           "tags": ["Tech", "Health"],
                                           "topic": "Scrum"}])