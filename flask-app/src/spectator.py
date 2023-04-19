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
    json_data = {}
    theData = cursor.fetchall()
    throws = {}
    for row in theData:
        throws[row[0]] = row[1]
    json_data['throwCounts'] = throws

    cursor.execute("SELECT gameID FROM GamesPlayed \
                WHERE player1ID = %s AND ((player1Throw = 'Rock' AND player2Throw = 'Scissors') OR (player1Throw = 'Scissors' AND player2Throw = 'Paper') OR (player1Throw = 'Paper' AND player2Throw = 'Rock')) \
                UNION ALL \
                SELECT gameID as Throw FROM GamesPlayed \
                WHERE player2ID = %s AND ((player2Throw = 'Rock' AND player1Throw = 'Scissors') OR (player2Throw = 'Scissors' AND player1Throw = 'Paper') OR (player2Throw = 'Paper' AND player1Throw = 'Rock'))" % (playerID, playerID))
    json_data['winCount'] = cursor.rowcount

    cursor.execute("SELECT gameID FROM GamesPlayed \
                    WHERE player1ID = %s \
                    UNION ALL \
                    SELECT gameID as Throw FROM GamesPlayed \
                    WHERE player2ID = %s" % (playerID, playerID))
    json_data['gamesPlayed'] = cursor.rowcount

    if json_data['gamesPlayed'] == 0:
        json_data['winPercent'] = 0
    else:
        json_data['winPercent'] = (
            json_data['winCount'] / json_data['gamesPlayed']) * 100

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
    json_data = {}
    theData = cursor.fetchall()
    throws = {}
    for row in theData:
        throws[row[0]] = row[1]
    json_data['throwCounts'] = throws

    cursor.execute(
        "SELECT gameID FROM GamesPlayed WHERE team1 = '%s' \
        UNION ALL \
        SELECT gameID  FROM GamesPlayed WHERE team2 = '%s'" % (teamName, teamName))
    json_data['gamesPlayed'] = cursor.rowcount

    cursor.execute("SELECT gameID FROM GamesPlayed \
                WHERE team1 = '%s' AND ((player1Throw = 'Rock' AND player2Throw = 'Scissors') OR (player1Throw = 'Scissors' AND player2Throw = 'Paper') OR (player1Throw = 'Paper' AND player2Throw = 'Rock')) \
                UNION ALL \
                SELECT gameID as Throw FROM GamesPlayed \
                WHERE team2 = '%s' AND ((player2Throw = 'Rock' AND player1Throw = 'Scissors') OR (player2Throw = 'Scissors' AND player1Throw = 'Paper') OR (player2Throw = 'Paper' AND player1Throw = 'Rock'))" % (teamName, teamName))
    json_data['winCount'] = cursor.rowcount
    if json_data['gamesPlayed'] == 0:
        json_data['winPercent'] = 0
    else:
        json_data['winPercent'] = (
            json_data['winCount'] / json_data['gamesPlayed']) * 100

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@spectator.route('/statistics/tournament/<tournamentID>', methods=["GET"])
def getTournamentStats(tournamentID):
    cursor = db.get_db().cursor()
    cursor.execute(
        "SELECT COUNT(tournamentID) as GamesPlayed FROM GamesPlayed WHERE tournamentID = %s" % (tournamentID))
    json_data = {}
    json_data['gamesPlayed'] = cursor.rowcount

    cursor.execute("SELECT team1 as team FROM GamesPlayed WHERE tournamentID = %s \
                   UNION \
                   SELECT team2 as team FROM GamesPlayed WHERE tournamentID = %s" % (tournamentID, tournamentID))
    json_data['teamsParticipated'] = [team[0] for team in cursor.fetchall()]

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@spectator.route('/statistics/season/<seasonID>', methods=["GET"])
def getSeasonStats(seasonID):
    cursor = db.get_db().cursor()
    cursor.execute(
        "SELECT COUNT(gameID) as GamesPlayed FROM GamesPlayed JOIN Tournament T on GamesPlayed.tournamentID = T.tournamentID WHERE T.season = %s" % (seasonID))
    json_data = {}
    json_data['gamesPlayed'] = cursor.rowcount

    cursor.execute("SELECT team FROM (SELECT team1 as team, tournamentID FROM GamesPlayed UNION SELECT team2 as team, tournamentID FROM GamesPlayed) games \
                    JOIN Tournament T on games.tournamentID = T.tournamentID \
                    WHERE T.season = %s;" % (seasonID))
    json_data['teamsParticipated'] = [team[0] for team in cursor.fetchall()]

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Tournaments and Seasons


@spectator.route('/tournaments', methods=["GET"])
def getTournaments():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Tournament')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@spectator.route('/seasons', methods=["GET"])
def getSeasons():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Season')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
