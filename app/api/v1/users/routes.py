"""The users meetup routes"""

from flask import jsonify, request
from app.admin.models import MeetupModel, MEETUPS_LEN
from app.api.v1 import path_1

@path_1.route("/meetups", methods=['POST'])
def admin_create_meetup():
  
   
    try:
        topic = request.get_json()['topic']
        happenningOn = request.get_json()['happenningOn']
        location = request.get_json()['location']
        images = request.get_json()['images']
        tags = request.get_json()['tags']

#return error message with the corresponding status code
    except:
        return jsonify({'status':400,
                        'error': 'Check the json keys you have used very well'}), 400

    if not topic:
        return jsonify({'status':400, 'error':'Provide the topic field'}), 400
    if not happenningOn:
        return jsonify({'status':400, 'error':'provide the meetup date'}), 400

    if not location:
        return jsonify({'status':400, 'error':'provide the location'}), 400

    if not tags:
        return jsonify({'status':400, 'error':'provide the tags'}), 400

    meetup = MeetupModel(
        topic=topic,
        happenningOn=happenningOn,
        location=location,
        images=images,
        tags=tags
    )
    meetup.save_meetup_record()

    #return a jsonify string with an OK status
    return jsonify({"status": 201,
                    "data": [{"topic": topic,
                              "location": location,
                              "happenningOn": happenningOn,
                              "images": images,
                              "tags": tags}]}), 201

#user gets a specific meetup record
@path_1.route("/meetups/<int:meetup_id>", methods=["GET"])
def get_specific_meetup(meetup_id):
    meetup = MeetupModel.get_specific_meetup(meetup_id)
    if meetup:
        return jsonify({"status": 200, "data": meetup}), 200
    return jsonify({"status": 404, "data": "Meetup not found"}), 404

#Get all upcoming meetup records
@path_1.route("/meetups/upcoming", methods=["GET"])
def get_all_upcoming_meetups():
    meetups = MeetupModel.get_all_upcoming_meetups()

    if meetups:
        return jsonify({"status": 200, "data": meetups}), 200
    return jsonify({
        "status": 404,
        "error": "No upcoming meetups available."
    }), 404