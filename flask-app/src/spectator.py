from flask import Blueprint, request, jsonify, make_response
import json
from src import db


spectator = Blueprint('spectator', __name__)

# --- FAVORITES ---


@spectator.route('/favoritePlayers/<user>', methods=["GET"])
def getFavoritePlayers(user):
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


@spectator.route('/favoritePlayers/<user>/<playerID>', methods=["POST"])
def insertFavoritePlayer(user, playerID):
    query = "INSERT INTO SpectatorFavPlayers (userName, playerID) VALUES ('%s', '%s')" % (
        user, playerID)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_response = make_response()
    the_response.status_code = 200 if cursor.rowcount == 1 else 400
    db.get_db().commit()
    return the_response


@spectator.route('/favoritePlayers/<user>/<playerID>', methods=["DELETE"])
def deleteFavoritePlayer(user, playerID):
    query = "DELETE FROM SpectatorFavPlayers WHERE userName = '%s' AND playerID = %s" % (
        user, playerID)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_response = make_response()
    the_response.status_code = 200 if cursor.rowcount == 1 else 400
    db.get_db().commit()
    return the_response


@spectator.route('/favoriteTeams/<user>', methods=["GET"])
def getFavoriteTeams(user):
    cursor = db.get_db().cursor()
    cursor.execute(
        'select teamName from SpectatorFavTeams WHERE userName = "%s"' % user)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@spectator.route('/favoriteTeams/<user>/<teamName>', methods=["POST"])
def insertFavoriteTeams(user, teamName):
    query = "INSERT INTO SpectatorFavTeams (userName, teamName) VALUES ('%s', '%s')" % (
        user, teamName)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_response = make_response()
    the_response.status_code = 200 if cursor.rowcount == 1 else 400
    db.get_db().commit()
    return the_response


@spectator.route('/favoriteTeams/<user>/<teamName>', methods=["DELETE"])
def deleteFavoriteTeams(user, teamName):
    query = "DELETE FROM SpectatorFavTeams WHERE userName = '%s' AND teamName = '%s'" % (
        user, teamName)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_response = make_response()
    the_response.status_code = 200 if cursor.rowcount == 1 else 400
    db.get_db().commit()
    return the_response


# --- STATISTICS ---

@spectator.route('/statistics/player/<playerID>', methods=["GET"])
def getPlayerStats(playerID):
    cursor = db.get_db().cursor()
    cursor.execute(
        'SELECT Throw, COUNT(Throw) as Count FROM (SELECT player1Throw as Throw FROM GamesPlayed WHERE player1ID = %s \
        UNION ALL \
        SELECT player2Throw as Throw FROM GamesPlayed WHERE player2ID = %s) allThrows \
        GROUP BY Throw' % (playerID, playerID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@spectator.route('/statistics/team/<teamName>', methods=["GET"])
def getTeamStats(teamName):
    cursor = db.get_db().cursor()
    cursor.execute(
        "SELECT Throw, COUNT(Throw) as Count FROM (SELECT player1Throw as Throw FROM GamesPlayed WHERE team1 = '%s' \
        UNION ALL \
        SELECT player2Throw as Throw FROM GamesPlayed WHERE team2 = '%s') allThrows \
        GROUP BY Throw" % (teamName, teamName))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@spectator.route('/statistics/tournament/<tournamentID>', methods=["GET"])
def getTournamentStats(tournamentID):
    cursor = db.get_db().cursor()
    cursor.execute(
        "SELECT COUNT(tournamentID) as GamesPlayed FROM GamesPlayed WHERE tournamentID = %s" % (tournamentID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@spectator.route('/statistics/season/<seasonID>', methods=["GET"])
def getSeasonStats(seasonID):
    cursor = db.get_db().cursor()
    cursor.execute(
        "SELECT COUNT(gameID) as GamesPlayed FROM GamesPlayed JOIN Tournament T on GamesPlayed.tournamentID = T.tournamentID WHERE T.season = %s" % (seasonID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
