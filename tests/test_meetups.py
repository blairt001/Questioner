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
       

        #sets up sign-up real admin
        self.signup_real_admin = {"firstname":"Andela",
                                  "lastname": "Lover",
                                  "username":"blairtheadmin",
                                  "email":"blair@gmail.com",
                                  "password": "Blairt123",
                                  "confirm_password":"Blairt123"}

        #logs in the real admin
        self.login_real_admin= {"username":"blairtheadmin",
                                "password":"Blairt123"}
        #sign-u fake admin
        self.signup_fake_admin = {"firstname":"Andela",
                            "lastname": "Lover",
                            "username":"fakedmin",
                            "email":"blair1@gmail.com",
                            "password": "Blairt123",
                            "confirm_password":"Blairt123"}

        #logs in fake admin
        self.login_fake_admin= {"username":"fakedmin",
                           "password":"Blairt123"}

        #declare login token to None
        self.token = ''

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
        self.rsvp_response1 = [{"Attending": "yes",
                                "meetup": 1,
                                "topic": "Scrum"}]

        self.meetup_record_topic = {"topic":"",
                            "happenningOn":"14/02/2019",
                            "location":"Thika",
                            "images":["blair.png", "tony.png"],
                            "tags":["Tech", "Health"]
                           }

        self.meetup_record_date = {"topic":"Scrum",
                            "happenningOn":"",
                            "location":"Thika",
                            "images":["blair.png", "tony.png"],
                            "tags":["Tech", "Health"]}

        self.meetup_record_location = {"topic":"Scrum",
                            "happenningOn":"14/02/2019",
                            "location":"",
                            "images":["blair.png", "tony.png"],
                            "tags":["Tech", "Health"]
                           }

        self.meetup_record_tag = {"topic":"Scrum",
                            "happenningOn":"14/02/2019",
                            "location":"Thika",
                            "images":["blair.png", "tony.png"],
                            "tags":[]
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

    #tear down tests                                 
    def tearDown(self):
        """Tperform final cleanup after tests run"""
        self.app.testing = False    

class TestMeetupsRecords(MeetupsBaseTest):
    """
    We test for all the meetup endpoints
    """
    

    #log in a fake admin
    def fake_admin_login(self):
        self.client.post(
            'api/v1/auth/signup', data=json.dumps(self.signup_real_admin), content_type="application/json")
        login = self.client.post(
            'api/v1/auth/login', data=json.dumps(self.login_real_admin), content_type="application/json")
        data = json.loads(login.data.decode('utf-8'))
        self.token = data["token"]
        return self.token

    #tests admin can create a meetup record
    def test_admin_can_create_a_meetup(self):
        response = self.client.post("api/v1/meetups",data = json.dumps(self.post_meetup1), headers={'x-access-token': self.token}, content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["data"], [{"location": "Thika","happenningOn": "14/02/2019","images": ["blair.png","tony.png"],"tags": ["Tech","Health"],"topic": "Scrum"}])
    
    #tests admin can delete a meetup record
    def test_admin_can_delete_a_meetup_record(self):
        self.token = self.fake_admin_login()
        self.client.post("api/v1/meetups", data = json.dumps(self.post_meetup1), headers={'x-access-token': self.token}, content_type = "application/json")
        response = self.client.delete("api/v1/meetups/1", headers={'x-access-token': self.token}, content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["data"], "Meetup Record Deleted Successfully")
    
    #tests user can fetch a specific meetup record
    def test_user_get_specific_meetup(self):
        self.client.post("api/v1/meetups", data = json.dumps(self.post_meetup1), headers={'x-access-token': self.token}, content_type = "application/json")
        self.client.post("api/v1/meetups", data = json.dumps(self.post_meetup2),  headers={'x-access-token': self.token}, content_type = "application/json")
        response = self.client.get("api/v1/meetups/1", content_type = "application/json")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['data'], [{"id": 1,
                                           "location":"Thika",
                                           "happenningOn":"14/02/2019",
                                           "tags": ["Tech", "Health"],
                                           "topic":"Scrum"}])
    
    #tests user can get all meetup records
    def test_user_can_get_all_meetups_records(self):
        self.client.post("api/v1/meetups", data = json.dumps(self.post_meetup1), headers={'x-access-token': self.token}, content_type = "application/json")
        self.client.post("api/v1/meetups", data = json.dumps(self.post_meetup2),  headers={'x-access-token': self.token}, content_type = "application/json")
        response = self.client.get("api/v1/meetups/upcoming", content_type = "application/json")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["status"], 200)
        # self.assertEqual(result["data"], self.meetups)

    #tests meetup topic required
    def test_meetup_topic_not_set(self):
        self.token = self.fake_admin_login()
        response = self.client.post("api/v1/meetups", data = json.dumps(self.meetup_record_topic), headers={'x-access-token': self.token}, content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["error"], 'Provide the topic field')

    #tests meetup date required
    def test_no_meetup_date_provided(self):
        self.token = self.fake_admin_login()
        response = self.client.post("api/v1/meetups", data = json.dumps(self.meetup_record_date), headers={'x-access-token': self.token}, content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["error"], 'Provide the meetup date')
    
    #tests for location required field
    def test_no_meetup_location_data_provided(self):
        self.token = self.fake_admin_login()
        response = self.client.post("api/v1/meetups", data = json.dumps(self.meetup_record_location), headers={'x-access-token': self.token}, content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["error"], 'provide the location')
    
    #tests for meetup record tag required
    def test_no_meetup_record_tags_data_provided(self):
        self.token = self.fake_admin_login()
        response = self.client.post("api/v1/meetups", data = json.dumps(self.meetup_record_tag), headers={'x-access-token': self.token}, content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["error"], 'provide the tags')

    #ttests for meetup record missing
    def test_meetup_record_missing(self):
        self.token = self.fake_admin_login()
        self.client.post("api/v1/meetups", data = json.dumps(self.post_meetup1), headers={'x-access-token': self.token}, content_type = "application/json")
        response = self.client.delete("api/v1/meetups/100", headers={'x-access-token': self.token}, content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(result["status"], 404)
        self.assertEqual(result["data"], "The specified meetup id 100 is missing from our database")
    
    
    #tests fo user rsvp a response, post their attendance status
    def test_user_can_confirm_rsvp_response(self):
        self.client.post("api/v1/meetups", data = json.dumps(self.post_meetup2),  content_type = "application/json")
        response = self.client.post("api/v1/meetups/1/rsvps/yes", content_type = "application/json")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['data'], self.rsvp_response1)
    