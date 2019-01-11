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
        self.upvoted_question= {"body": "I really like how people talk about Andela's Scrum",
                                "meetup_id": 1,
                                "question_id": 1,
                                "title": "What is Scrum?",
                                "votes": 1}
        self.downvoted_question = {"body": "I really like how people talk about Andela's Scrum",
                                   "meetup_id": 1,
                                   "question_id": 1,
                                   "title": "What is Scrum?",
                                   "votes": -1}
        #prepare questions setup
        self.post_question1 = {"title":"What is Scrum?",
                               "body":"I really like how people talk about Andela's Scrum"}

        self.post_question2 = {"title":"What is JWT?",
                               "body":"I learnt more about JWT at Andela's bootcamp"}


        self.post_comment = {"comment":"I would love to hear this question answered"}

        self.question_and_comment = {"body": "I would like to know this",
                                     "comments": ["I would love to hear this question answered"],
                                     "meetup_id": 1,
                                     "question_id": 1,
                                     "title": "what are languages?",
                                     "votes": 0}

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