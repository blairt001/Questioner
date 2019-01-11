import json
import unittest

# local imports
from app import create_app

class QuestionBaseTest(unittest.TestCase):
    """
    Setting up tests
    """

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.meetup = {"topic":"Scrum",
                       "happenningOn":"14/02/2019",
                       "location":"Thika",
                       "images":["tony.png", "blair.png"],
                       "tags":["Tech", "Health"]
                      }

        self.post_question1 = {"title":"What is Scrum?",
                               "body":"I really like how people talk about Andela's Scrum"}

        self.post_question2 = {"title":"What is JWT?",
                               "body":"I learnt more about JWT at Andela's bootcamp"}

        self.upvoted_question= {"body": "I really like how people talk about Andela's Scrum",
                                "meetup_id": 1,
                                "comments": [], #initialize comments to an empty list
                                "question_id": 1,
                                "title": "What is Scrum?",
                                "votes": 1}
        self.downvoted_question = {"body": "I really like how people talk about Andela's Scrum",
                                   "meetup_id": 1,
                                   "comments": [],  #initialize comments to an empy list
                                   "question_id": 1,
                                   "title": "What is Scrum?",
                                   "votes": -1}
        #prepare comments setup
        self.post_comment1 = {"comment":"Wow, I love every topic on scrum, the answer will help me alot"}

        self.question1_and_comment1 = {"body": "I really like how people talk about Andela's Scrum",
                                     "comments": ["Wow, I love every topic on scrum, the answer will help me alot"],
                                     "meetup_id": 1,
                                     "question_id": 1,
                                     "title": "What is Scrum?",
                                     "votes": 0}
    #tear down tests                                 
    def tearDown(self):
        """Tperform final cleanup after tests run"""
        self.app.testing = False
        

class TestQuestionApiEndpoint(QuestionBaseTest):
    """
    Asserts whether the endpoints are working or not
    """
    def test_user_can_post_a_question_to_meetup(self):
        """
        test to return success
        """
        self.client.post("api/v1/meetups", data = json.dumps(self.meetup), content_type = "application/json")
        response = self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.post_question1), content_type = "application/json")
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['status'], 201)
        self.assertEqual(result['data'], [{"body": "I really like how people talk about Andela's Scrum",
                                           "meetup": 1,
                                           "title": "What is Scrum?"}])

    def test_upvote_question(self):
        """
        test a user can upvote a question
        """
        self.client.post("api/v1/meetups", data = json.dumps(self.meetup), content_type = "application/json")
        self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.post_question1), content_type = "application/json")
        response = self.client.patch("api/v1/questions/1/upvote", content_type = "application/json")
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['data'], self.upvoted_question)

    def test_downvote_question(self):
        """
        test a user can downvote a question
        """
        self.client.post("api/v1/meetups", data = json.dumps(self.meetup), content_type = "application/json")
        self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.post_question1), content_type = "application/json")
        response = self.client.patch("api/v1/questions/1/downvote", content_type = "application/json")
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['data'], self.downvoted_question)

    #define test case for user posting comments
    def test_user_comment_on_a_question(self):
        """
        tests that a user can actually comment on a question
        """
        self.client.post("api/v1/meetups", data = json.dumps(self.meetup), content_type = "application/json")
        self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.post_question1), content_type = "application/json")
        response = self.client.post("api/v1/questions/1/comment", data = json.dumps(self.post_comment1), content_type = "application/json")
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data.decode("utf'8"))
        self.assertEqual(result['data'], self.question1_and_comment1)

    def test_get_all_questions_records(self):
        """
        User should be able to get all the questions records
        """
        self.client.post("api/v1/meetups", data = json.dumps(self.meetup), content_type = "application/json")
        self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.post_question1), content_type = "application/json")
        self.client.post("api/v1/meetups/1/questions", data = json.dumps(self.post_question2), content_type = "application/json")
        response = self.client.get("api/v1/meetups/1/questions", content_type = "application/json")
        self.assertEqual(response.status_code, 200)