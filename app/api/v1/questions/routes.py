"""The users meetup routes"""

from flask import jsonify, request
from app.users.models import QuestionModel, QUESTIONS_LEN
from app.api.v1 import path_1

@path_1.route("/meetups/<int:meetup_id>/questions", methods=['POST'])
def create_question_record(meetup_id):
    try:
        title = request.get_json()['title']
        body = request.get_json()['body']

    except:
        return jsonify({'status': 400,
                        ' error': "Check your json keys. Should be topic and body"})

    if not title:
        return jsonify({'status': 400,
                        'error': 'topic field is required'})

    if not body:
        return jsonify({'status': 400,
                        'error': 'body field is required'})

    question = QuestionModel(title=title,
                        body=body,
                        meetup_id=meetup_id)

    question.save_question()

    return jsonify({"status": 201,
                    "data":[{"title": title,
                             "meetup": meetup_id,
                             "body": body}]}), 201