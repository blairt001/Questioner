"""
The admin meetup model
"""
#import date
from datetime import datetime

#assign meetups to an empty list
MEETUPS_LEN = []

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