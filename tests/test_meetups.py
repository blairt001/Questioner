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

        self.signup_admin_user1 = {"firstname":"Tony",
                             "lastname": "Andela",
                             "username":"blairtheadmin",
                             "email":"blair1234@gmail.com",
                             "password": "Blairman1234",
                             "confirm_password":"Blairman1234"}

        self.signup_admin_user2 = {"firstname":"Tony",
                             "lastname": "Andela",
                             "username":"fakeadmin",
                             "email":"blair1234.dev@gmail.com",
                             "password": "Blairman1234",
                             "confirm_password":"Blairman1234"}

        self.login_user1 = {"username":"blairtheadmin",
                           "password":"Blairman1234"}

        self.login_user2 = {"username":"fakeadmin",
                           "password":"Blairman1234"}



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
        self.post_meetup3 = {"topic":"Miguel Miguel",
                             "happenningOn":"16/02/2019",
                             "location":"Nairobi",
                             "images":["mig1.png", "mig2.png"],
                             "tags":["Tech", "Health"]
                            }
        
        self.post_meetup4 = {"topic":"Miguel Brings",
                             "happenningOn":"16/02/2019",
                             "location":"Nairobi",
                             "images":["mig1.png", "mig2.png"],
                             "tags":["Tech", "Health"]
                            }

        self.post_meetup5 = {"topic":"Andela Fellowship",
                             "happenningOn":"16/02/2019",
                             "location":"Nairobi",
                             "images":["mig1.png", "mig2.png"],
                             "tags":["Tech", "Health"]
                            }

        self.rsvp_response1 = [{"Attending": "yes",
                                "meetup": 4,
                                "topic": "Miguel Brings"}]

        self.rsvp_response2 = [{"Attending": "yes",
                                "meetup": 5,
                                "topic": "Andela Fellowship"}]

        self.specific_meetup = [{
                                "id": 5,
                                "happenningOn": "16/02/2019",
                                "location": "Nairobi",
                                "tags": ["Tech","Health"],
                                 "topic": "Andela Fellowship"
                                }]
                                                            

        self.meetup_topic_record = {"topic":"",
                            "happenningOn":"14/02/2019",
                            "location":"Thika",
                            "images":["blair.png", "tony.png"],
                            "tags":["Tech", "Health"]}

        self.meetup_location_record = {"topic":"Scrum",
                            "happenningOn":"14/02/2019",
                            "location":"",
                            "images":["blair.png", "tony.png"],
                            "tags":["Tech", "Health"]}

        self.meetup_date_record = {"topic":"Scrum",
                            "happenningOn":"",
                            "location":"Thika",
                            "images":["blair.png", "tony.png"],
                            "tags":["Tech", "Health"]}

        self.meetup_tag_record = {"topic":"Scrum",
                            "happenningOn":"14/02/2019",
                            "location":"Thika",
                            "images":["blair.png", "tony.png"],
                            "tags":[]}


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

        self.token = ''

    #tear down tests                                 
    def tearDown(self):
        """Tperform final cleanup after tests run"""
        self.app.testing = False    

class TestMeetupsRecords(MeetupsBaseTest):
    """
    We test for all the meetup endpoints
    """
    def admin_login(self):
        self.client.post(
            'api/v1/auth/signup', data=json.dumps(self.signup_admin_user1), content_type="application/json")
        login = self.client.post(
            'api/v1/auth/login', data=json.dumps(self.login_user1), content_type="application/json")
        data = json.loads(login.data.decode('utf-8'))
        self.token = data["token"]
        return self.token

    def test_admin_can_create_a_meetup(self):

        """ Test for admin creating a meetup"""
        self.token = self.admin_login()
        response = self.client.post("api/v1/meetups",data = json.dumps(self.post_meetup1),headers={'x-access-token': self.token}, content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["data"], [{"location": "Thika","happenningOn": "14/02/2019","images": ["blair.png","tony.png"],"tags": ["Tech","Health"],"topic": "Scrum"}])
 
    
    def test_user_can_get_all_meetups_records(self):
        """
       User to fetch all upcoming meetup records
        """
        self.client.post("api/v1/meetups", data = json.dumps(self.post_meetup1),headers={'x-access-token': self.token}, content_type = "application/json")
        self.client.post("api/v1/meetups", data = json.dumps(self.post_meetup2), headers={'x-access-token': self.token}, content_type = "application/json")

        response = self.client.get("api/v1/meetups/upcoming", content_type = "application/json")
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["status"], 200)
        # self.assertEqual(result["data"], self.meetups)
    

    
    #tests for meetup not set
    def test_no_meetup_topic_provided(self):
        self.token = self.admin_login()
        response = self.client.post("api/v1/meetups", data = json.dumps(self.meetup_topic_record),headers={'x-access-token': self.token}, content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["error"], 'Provide the topic field')
    
    #tests for meetup location missing
    def test_no_meetup_location_provided(self):
        self.token = self.admin_login()
        response = self.client.post("api/v1/meetups", data = json.dumps(self.meetup_location_record), headers={'x-access-token': self.token}, content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["error"], 'provide the location')

    #tests for meetup date missing
    def test_no_meetup_date_provided(self):
        self.token = self.admin_login()
        response = self.client.post("api/v1/meetups", data = json.dumps(self.meetup_date_record),headers={'x-access-token': self.token}, content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["error"], 'provide the meetup date')

    #tests for meetup tags missing
    def test_no_meetup_tags_provided(self):
        self.token = self.admin_login()
        response = self.client.post("api/v1/meetups", data = json.dumps(self.meetup_tag_record), headers={'x-access-token': self.token}, content_type = "application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["error"], 'provide the tags')

    #tests admin can delete a meetup record
    
    def test_meetup_record_not_found(self):
        """
        Test response when a meetup is not found
        """
        self.token = self.admin_login()
        self.client.post("api/v1/meetups",
                         data=json.dumps(self.post_meetup1),
                         headers={'x-access-token': self.token},
                         content_type="application/json")
        response = self.client.delete("api/v1/meetups/50",
                                      headers={'x-access-token': self.token},
                                      content_type="application/json")
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(result["status"], 404)
        self.assertEqual(result["data"], "Meetup with id 50 not found")

    def test_user_get_a_specific_meetup(self):
        #self.token = self.admin_login
        self.client.post("api/v1/meetups",
                         data=json.dumps(self.post_meetup1),
                         headers={'x-access-token': self.token},
                         content_type="application/json")
        self.client.post("api/v1/meetups",
                         data=json.dumps(self.post_meetup2),
                         headers={'x-access-token': self.token},
                         content_type="application/json")
        self.client.post("api/v1/meetups",
                         data=json.dumps(self.post_meetup3),
                         headers={'x-access-token': self.token},
                         content_type="application/json")
        self.client.post("api/v1/meetups",
                         data=json.dumps(self.post_meetup4),
                         headers={'x-access-token': self.token},
                         content_type="application/json")
        self.client.post("api/v1/meetups",
                         data=json.dumps(self.post_meetup5),
                         headers={'x-access-token': self.token},
                         content_type="application/json")

        response = self.client.get("api/v1/meetups/5",
                                   content_type="application/json")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['data'], self.specific_meetup)

    def test_user_can_set_rsvp_response(self):
        """
        Tests to show a user can successfully confirm ther attendance status
        """
        #self.token = self.admin_login()
        self.client.post("api/v1/meetups",
                         data=json.dumps(self.post_meetup5),
                         headers={'x-access-token': self.token},
                         content_type="application/json")
        response = self.client.post("api/v1/meetups/5/rsvps/yes",content_type="application/json")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['data'], self.rsvp_response2)

        
