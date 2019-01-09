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
                               "body":"I really like how people talk about Andela"}
