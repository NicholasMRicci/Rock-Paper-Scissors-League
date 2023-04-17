from flask import Blueprint, request, jsonify, make_response
import json
from src import db

# Create a new Flask Blueprint
# IMPORTANT: Notice in the routes below, we are adding routes to the
# blueprint object, not the app object.
matches = Blueprint('matches', __name__)


@matches.route('/', methods=["GET"])
def home():
    cursor = db.get_db().cursor()
    cursor.execute('select * from GamesPlayed')
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


@matches.route('/', methods=["POST"])
def insert():
    data = request.json
    gameID = data["gameID"]
    player1ID = data["player1ID"]
    player1Throw = data["player1Throw"]
    player2ID = data["player2ID"]
    player2Throw = data["player2Throw"]
    team1 = data["team1"]
    team2 = data["team2"]
    tournamentID = data["tournamentID"]
    query = "INSERT INTO GamesPlayed (gameID, player1ID, player1Throw, player2ID, player2Throw, team1, team2, tournamentID) VALUES (%i, %i, '%s', %i, '%s', '%s', '%s', %i)" % (
        gameID, player1ID, player1Throw, player2ID, player2Throw, team1, team2, tournamentID)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_response = make_response()
    the_response.status_code = 200 if cursor.rowcount == 1 else 301
    db.get_db().commit()
    return the_response

# {
#     "gameID": 1,
#     "player1ID": 3,
#     "player1Throw": "Scissors",
#     "player2ID": 4,
#     "player2Throw": "Rock",
#     "team1": "Team2",
#     "team2": "Team8",
#     "tournamentID": 1
#   },
