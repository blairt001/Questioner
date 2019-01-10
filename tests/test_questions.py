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

        self.post_question1 = {"title":"What is scrum?",
                               "body":"I really like how people talk about Andela's Scrum"}
        self.upvoted_question= {"body": "I really like how people talk about XYZ",
                                "meetup_id": 1,
                                "question_id": 1,
                                "title": "What is   XYZ?",
                                "votes": 1}
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
                                           "title": "What is scrum?"}])

   

