"""The meetup routes"""

from flask import jsonify, request
from app.admin.models import MeetupModel
from app.api.v1 import path_1

@path_1.route("/meetups", methods=['POST'])
def admin_create_meetup():
    """
    POST a meetup : POST admin/meetups
    """
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