from flask import Blueprint, request, jsonify, make_response
import json
from src import db

# Create a new Flask Blueprint
# IMPORTANT: Notice in the routes below, we are adding routes to the
# blueprint object, not the app object.
coaches = Blueprint('coaches', __name__)


@coaches.route('/', methods=["GET"])
def home():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Coaches')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    # extra
    return the_response


@coaches.route('/', methods=["POST"])
def make_new():
    data = request.json
    cursor = db.get_db().cursor()
    cursor.execute("INSERT INTO Coaches (firstName, lastName, joinDate, birthday, phoneNumber) \
                   VALUES ('{}', '{}', '{}', '{}', '{}')"
                   .format(data['firstName'], data['lastName'], data['joinDate'], data['birthday'], data['phoneNumber']))
    result = cursor.rowcount
    if result == 1:
        db.get_db().commit()
        return make_response('ok', 200)
    return make_response('not ok: ', 301)


@coaches.route('/<coachID>', methods=["GET"])
def getID(coachID):
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM Coaches WHERE coachID = {}"
                   .format(coachID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
