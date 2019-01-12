"""
The admin meetup model
"""
#import date
from datetime import datetime

#assign meetups_len, questions_len, comments_len and users_len to an empty list
MEETUPS_LEN = []
QUESTIONS_LEN = []
COMMENTS_LEN = []
USERS_LEN = []

#create the meetup model class
class MeetupModel:
    def __init__(self, topic, happenningOn, location, images, tags):
        """
       Initialize the meetup class, with your variables at hand
        """
        self.id = len(MEETUPS_LEN)+1
        self.topic = topic
        self.happenningOn = happenningOn
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

    @staticmethod
    def get_all_upcoming_meetups():
        """
        gets all meetups
        """
        return [MeetupModel.to_json(meetup) for meetup in MEETUPS_LEN]

    #staticmethod decorator
    #convert the meetup record to JSON format
    #let the dict be readable
    #Ignore images and created_at
    @staticmethod
    def to_json(meetup):
        return {
            "id": meetup.id,
            "topic": meetup.topic,
            "happenningOn": meetup.happenningOn,
            "location": meetup.location,
            "tags": meetup.tags,
        }

class QuestionModel:
    def __init__(self, title, body, meetup_id):
        """
        The initialization of the Question class that defines its variables
        """
        self.question_id = len(QUESTIONS_LEN)+1
        self.meetup_id = meetup_id
        self.title = title
        self.votes = 0
        self.body = body
        self.comments = COMMENTS_LEN
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
            "comments": question.comments
        }
    @staticmethod
    def get_question(quiz_id):
        """
        fetch a specific question using its id
        """
        return [QuestionModel.to_json(question) for question in QUESTIONS_LEN if question.question_id == quiz_id]

    @staticmethod
    def get_all_questions(meeting_id):
        """
        user get all questions asked for the meetup
        """
        return [QuestionModel.to_json(question) for question in QUESTIONS_LEN if question.meetup_id == meeting_id]
#Comment model class
class CommentModel:
    """
    This is the model class for holding comment fields
    """

    def __init__(self, comment, question_id):
        self.comment = comment
        self.comment_id = len(COMMENTS)+1
        self.question_id = question_id

    def save_comment(self):
        """
        Save the comment to the comments structure
        """
        COMMENTS_LEN.append(self)

    
    @staticmethod    #module level function
    def to_json(comment):
        """
        Convert the comment object to json, a readable dict
        """
        return {"comment":comment.comment,
                "comment_id":comment.comment_id,
                "question_id":comment.question}

class UserModel:
    """
    This is the user model class that contains our model setup
    """

    def __init__(self, firstname, username, lastname, email, password):
        """
        Start by defining each user attributes to use during the tests
        Keep in mind the user is not an admin
        """
        self.user_id = len(USERS_LEN)+1
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.registered_on = datetime.now()
        self.password = password
        self.is_admin = False

    #after sign-up save the user to the created dict , USERS_LEN
    def save_user(self):
        """
        Add a new user to the users store
        """
        USERS_LEN.append(self)

    #lets check the data store for any user
    @staticmethod
    def query_users(username, password):
        return [UserModel.to_json(user) for user in USERS_LEN if user.username == username and user.password == password]

    #return a json data , a readable dictionary object, including the date user was registered
    @staticmethod
    def to_json(user):
        return {"firstname": user.firstname,
                "lastname": user.lastname,
                "username": user.username,
                "email": user.email,
                "password": user.password,
                "registered_on": user.registered_on,}


