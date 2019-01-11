"""The users meetup routes"""

from flask import jsonify, request
from app.admin.models import QuestionModel, QUESTIONS_LEN, MeetupModel, MEETUPS_LEN, CommentModel, COMMENTS_LEN
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
#upvote a question
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

#downvote a question
@path_1.route("/questions/<int:question_id>/downvote", methods=['PATCH'])
def downvote_question(question_id):
    """
    The downvote question route endpoint
    """
    question = QuestionModel.get_question(question_id)
    if question:
        my_question = question[0]
        my_question['votes'] = my_question['votes'] - 1
        return jsonify({"status": 200, "data": my_question}), 200
    return jsonify({"status": 404, "error": "Question not found"}), 404

#user should be able to post comment
@path_1.route("/questions/<int:question_id>/comment", methods=['POST'])
def user_comment_on_a_question(question_id):
    """
    User post comment endpoint route
    """
    try:
        comment = request.get_json()['comment']
    except KeyError:
        abort(make_response(jsonify({'status': 400, 'error':'Check your json key. It is comment'})))
    question = QuestionModel.get_question(question_id)
    if question:
        my_question = question[0]
        my_question['comments'].append(comment)
        return jsonify({"status": 201, "data": my_question}), 201
    return jsonify({'status': 404, 'error':'The question you are looking for is not found'}), 404

@path_1.route("/meetups/<int:meet_id>/questions", methods=['GET'])
def get_user_get_all_questions_for_a_meetup(meet_id):
    """
    User to fetch all questions for a meetup record
    """
    questions = QuestionModel.get_all_questions(meet_id)
    if questions:
        return jsonify({"status": 200, "data": questions}), 200
    return jsonify({"status": 404, "data": "We cant find a question for this meetup. No question posted yet"}), 404