"""
The users meetup model
"""
#import date
from datetime import datetime

#assign meetups to an empty list
MEETUPS_LEN = []
QUESTIONS_LEN = []
#create the meetup model class
class MeetupModel:
    def __init__(self, topic, happenningOn, location, images, tags):
        """
       Initialize the meetup class, with your variables at hand
        """
        self.id = len(MEETUPS_LEN)+1
        self.topic = topic
        self.happeningOn = happenningOn
        self.location = location
        self.images = images
        self.tags = tags
        self.created_at = datetime.now()

    def save_meetup_record(self):
        """
        save a new meetup record 
        """
        MEETUPS_LEN.append(self)

    @staticmethod
    def get_specific_meetup(meeting_id):
        """
        get a specific meetup record using its meetup id
        """
        return [MeetupModel.to_json(meetup) for meetup in MEETUPS_LEN if meetup.id == meeting_id]

    #staticmethod decorator
    #convert the meetup record to JSON format
    #let the dict be readable
    @staticmethod
    def to_json(meetup):
        return {
            "id": meetup.id,
            "topic": meetup.topic,
            "happenningOn": meetup.happenningOn,
            "location": meetup.location,
            "images": meetup.images,
            "tags": meetup.tags,
            "created_at": meetup.created_at
        }

class Question:
    def __init__(self, title, body, meetup_id):
        """
        The initialization of the Question class that defines its variables
        """
        self.question_id = len(QUESTIONS_LEN)+1
        self.meetup_id = meetup_id
        self.title = title
        self.votes = 0
        self.body = body
        self.created_at = datetime.now()

    def save_question(self):
        """
        saves the question to the question store
        """
        QUESTIONS_LEN.append(self)

    @staticmethod
    def to_json(question):
        """
        format question object to a readable dictionary
        """
        return {
            "question_id": question.question_id,
            "title": question.title,
            "meetup_id": question.meetup_id,
            "votes": question.votes,
            "body": question.body,
        }