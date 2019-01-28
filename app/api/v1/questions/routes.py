"""The users meetup routes"""

from flask import jsonify, request, make_response, abort
from app.admin.models import QuestionModel, QUESTIONS_LEN, MeetupModel, MEETUPS_LEN, CommentModel, COMMENTS_LEN
from app.api.v1 import path_1
from app.utils import token_required, decode_token


@path_1.route("/meetups/<int:meetup_id>/questions", methods=['POST'])
@token_required
def create_question_record(specific_user, meetup_id):
    try:
        data = request.get_json()
        title = data['title']
        body = data['body']

    except:
        return jsonify({'status': 400,
                        ' error': "Check your json keys. Should be topic and body"})

    if not title:
        return jsonify({'status': 400,
                        'error': 'topic field is required'})

    if not body:
        return jsonify({'status': 400,
                        'error': 'body field is required'})
    meetup = MeetupModel.get_specific_meetup(meetup_id)
    if not meetup:
        abort(make_response(jsonify({
            'status': 404, 'error': 'Meetup with id {} not found'.format(meetup_id)})))
    question = QuestionModel(title=title,
                             body=body,
                             meetup_id=meetup_id)

    question.save_question()

    return jsonify({"status": 201,
                    "data": [{"title": title,
                              "meetup": meetup_id,
                              "body": body}]}), 201
# upvote a question


@path_1.route("/questions/<int:question_id>/upvote", methods=['PATCH'])
@token_required
def upvote_question(specific_question, question_id):
    """
    The upvote question route endpoint
    """
    question = QuestionModel.get_question(question_id)
    if question:
        my_question = question[0]
        my_question['votes'] = my_question['votes'] + 1
        return jsonify({"status": 200, "data": my_question}), 200
    return jsonify({"status": 404, "error": "Question not found"}), 404

# downvote a question


@path_1.route("/questions/<int:question_id>/downvote", methods=['PATCH'])
@token_required
def downvote_question(specific_user, question_id):
    """
    The downvote question route endpoint
    """
    question = QuestionModel.get_question(question_id)
    if question:
        my_question = question[0]
        my_question['votes'] = my_question['votes'] - 1
        return jsonify({"status": 200, "data": my_question}), 200
    return jsonify({"status": 404, "error": "Question not found"}), 404

# user should be able to post comment


@path_1.route("/questions/<int:question_id>/comment", methods=['POST'])
@token_required
def user_comment_on_a_question(specific_user, question_id):
    """
    User post comment endpoint route
    """
    try:
        data = request.get_json()
        comment = data['comment']
    except KeyError:
        abort(make_response(jsonify({
            'status': 400, 'error': 'Check your json key. Should be comment'})))

    username = decode_token()

    question = QuestionModel.get_question(question_id)
    if question:
        my_question = question[0]
        comments = my_question['comments']
        comments.append(comment)
        comments.append(username)
        return jsonify({"status": 201, "data": my_question}), 201
    return jsonify({
        'status': 404, 'error': 'Question with id {} not found'.format(question_id)}), 404


@path_1.route("/meetups/<int:meet_id>/questions", methods=['GET'])
def get_user_get_all_questions_for_a_meetup(meet_id):
    """
    User to fetch all questions for a meetup record
    """
    questions = QuestionModel.get_all_questions(meet_id)
    if questions:
        return jsonify({"status": 200, "data": questions}), 200
    return jsonify({"status": 404, "data": "We cant find a question for this meetup. No question posted yet"}), 404
