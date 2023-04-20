from flask import Blueprint, request, jsonify, make_response
import json
from src import db


coach = Blueprint('coach', __name__)

# --- MATCH HISTORY ---


@coach.route('/matches', methods=["GET"])
def getMatches():
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
    return the_response


@coach.route('/matches/<gameID>', methods=["GET"])
def getMatch(gameID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from GamesPlayed WHERE gameID = %s' % (gameID))
    row_headers = [x[0] for x in cursor.description]
    theData = cursor.fetchall()
    if cursor.rowcount == 1:
        the_response = make_response(
            jsonify((dict(zip(row_headers, theData[0])))))
        the_response.status_code = 200
        the_response.mimetype = 'application/json'
        return the_response
    else:
        the_response = make_response()
        the_response.status_code = 400
        return the_response


@coach.route('/matches', methods=["POST"])
def insertMatch():
    data = request.json
    query = "INSERT INTO GamesPlayed (player1ID, player1Throw, player2ID, player2Throw, team1, team2, tournamentID) VALUES (%s, '%s', %s, '%s', '%s', '%s', %s)" % (
        data["player1ID"], data["player1Throw"], data["player2ID"], data["player2Throw"], data["team1"], data["team2"], data["tournamentID"])

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_response = make_response()
    the_response.status_code = 200 if cursor.rowcount == 1 else 400
    db.get_db().commit()
    return the_response


@coach.route('/matches/<gameID>', methods=["PUT"])
def updateMatch(gameID):
    data = request.json
    query = "UPDATE GamesPlayed SET player1ID = %s, player1Throw = '%s', player2ID = %s, player2Throw = '%s', team1 = '%s', team2 = '%s', tournamentID = %s WHERE gameID = %s" % (
        data["player1ID"], data["player1Throw"], data["player2ID"], data["player2Throw"], data["team1"], data["team2"], data["tournamentID"], gameID)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_response = make_response()
    the_response.status_code = 200 if cursor.rowcount == 1 else 400
    db.get_db().commit()
    return the_response


@coach.route('/matches/<gameID>', methods=["DELETE"])
def deleteMatch(gameID):
    query = "DELETE FROM GamesPlayed WHERE gameID = %s" % (
        gameID)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_response = make_response()
    the_response.status_code = 200 if cursor.rowcount == 1 else 400
    db.get_db().commit()
    return the_response

# --- PLAYERS ---


@coach.route('/players', methods=["GET"])
def getPlayers():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Players')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@coach.route('/players/<playerID>', methods=["GET"])
def getPlayer(playerID):
    cursor = db.get_db().cursor()
    cursor.execute(
        'select * from Players WHERE playerID = %s' % (playerID))
    row_headers = [x[0] for x in cursor.description]
    theData = cursor.fetchall()
    if cursor.rowcount == 1:
        the_response = make_response(
            jsonify((dict(zip(row_headers, theData[0])))))
        the_response.status_code = 200
        the_response.mimetype = 'application/json'
        return the_response
    else:
        the_response = make_response()
        the_response.status_code = 400
        return the_response


@ coach.route('/players', methods=["POST"])
def insertPlayer():
    data = request.json
    cursor = db.get_db().cursor()
    # work with adding in all player attributes
    cursor.execute("INSERT INTO Players (firstName, lastName, joinDate, birthday, phoneNumber, playerStatus) \
                   VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"
                   % (data['firstName'], data['lastName'], data['joinDate'], data['birthday'], data['phoneNumber'], data['playerStatus']))
    if cursor.rowcount == 1:
        db.get_db().commit()
        return make_response('ok', 200)
    return make_response('not ok: ', 301)


@ coach.route('/players/<playerID>', methods=["PUT"])
def updatePlayer(playerID):
    data = request.json
    cursor = db.get_db().cursor()
    # work with adding in all player attributes
    if "teamName" in data:
        cursor.execute("UPDATE Players SET firstName = '%s', lastName = '%s', joinDate = '%s', birthday = '%s', phoneNumber = '%s', playerStatus = '%s', teamName = '%s' WHERE playerID = %s"
                       % (data['firstName'], data['lastName'], data['joinDate'], data['birthday'], data['phoneNumber'], data['playerStatus'], data['teamName'], playerID))
    else:
        cursor.execute("UPDATE Players SET firstName = '%s', lastName = '%s', joinDate = '%s', birthday = '%s', phoneNumber = '%s', playerStatus = '%s', teamName = NULL WHERE playerID = %s"
                       % (data['firstName'], data['lastName'], data['joinDate'], data['birthday'], data['phoneNumber'], data['playerStatus'], playerID))
    if cursor.rowcount == 1:
        db.get_db().commit()
        return make_response('ok', 200)
    return make_response('not ok: ', 301)


@coach.route('/players/<playerID>', methods=["DELETE"])
def deletePlayer(playerID):
    query = "DELETE FROM Players WHERE playerID = %s" % (
        playerID)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    if cursor.rowcount == 1:
        db.get_db().commit()
        return make_response('ok', 200)
    return make_response('not ok: ', 301)


# --- TEAMS ---
@coach.route('/teams', methods=["GET"])
def getTeams():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Teams')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@coach.route('/teams/<teamName>', methods=["GET"])
def getTeam(teamName):
    cursor = db.get_db().cursor()
    cursor.execute(
        "select * from Teams WHERE teamName = '%s'" % (teamName))
    row_headers = [x[0] for x in cursor.description]
    theData = cursor.fetchall()
    if cursor.rowcount == 1:
        the_response = make_response(
            jsonify((dict(zip(row_headers, theData[0])))))
        the_response.status_code = 200
        the_response.mimetype = 'application/json'
        return the_response
    else:
        the_response = make_response()
        the_response.status_code = 400
        return the_response


@coach.route('/myTeam/<coachID>', methods=["GET"])
def getMyTeam(coachID):
    cursor = db.get_db().cursor()
    cursor.execute(
        'SELECT P.* FROM Teams JOIN Players P ON Teams.teamName = P.teamName WHERE Teams.coachID = %s' % (coachID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@coach.route('/myTeamName/<coachID>', methods=["GET"])
def getMyTeamName(coachID):
    cursor = db.get_db().cursor()
    cursor.execute(
        'SELECT teamName FROM Teams WHERE coachID = %s' % (coachID))
    json_data = cursor.fetchall()[0][0]
    the_response = make_response(json_data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Coaches


@coach.route('/coaches', methods=["GET"])
def getCoaches():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Coaches')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
