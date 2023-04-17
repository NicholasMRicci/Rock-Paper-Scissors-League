from flask import Blueprint, request, jsonify, make_response
import json
from src import db

# Create a new Flask Blueprint
# IMPORTANT: Notice in the routes below, we are adding routes to the
# blueprint object, not the app object.
favoritePlayers = Blueprint('favoritePlayers', __name__)


@favoritePlayers.route('/<user>', methods=["GET"])
def home(user):
    cursor = db.get_db().cursor()
    cursor.execute(
        'select playerID from SpectatorFavPlayers WHERE userName = "%s"' % user)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@favoritePlayers.route('/', methods=["POST"])
def insert():
    data = request.json
    user = data["userName"]
    team = data["playerID"]
    query = "INSERT INTO SpectatorFavPlayers (userName, playerID) VALUES ('%s', %i)" % (
        user, team)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_response = make_response()
    the_response.status_code = 200 if cursor.rowcount == 1 else 301
    db.get_db().commit()
    return the_response


@favoritePlayers.route('/', methods=["GET"])
def other():
    cursor = db.get_db().cursor()
    cursor.execute('select * from SpectatorFavPlayers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
