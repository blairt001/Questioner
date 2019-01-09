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
#upvote a given question
@path_1.route("/questions/<int:question_id>/upvote", methods=['PATCH'])
def upvote_question(question_id):
    """
    The upvote question route endpoint
    """
    question = QuestionModel.get_question(question_id)
    if question:
        my_question = question[0]
        my_question['votes'] = my_question['votes'] + 1
        return jsonify({"status": 200, "data": my_question}), 200
    return jsonify({"status": 404, "error": "Question not found"}), 404

#downvote a given question
@path_1.route("/questions/<int:question_id>/downvote", methods=['PATCH'])
def downvote_question(question_id):
    """
    The upvote question route endpoint
    """
    question = QuestionModel.get_question(question_id)
    if question:
        my_question = question[0]
        my_question['votes'] = my_question['votes'] + 1
        return jsonify({"status": 200, "data": my_question}), 200
    return jsonify({"status": 404, "error": "Question not found"}), 404