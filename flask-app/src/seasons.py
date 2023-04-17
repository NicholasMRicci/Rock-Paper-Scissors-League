from flask import Blueprint, request, jsonify, make_response
import json
from src import db

# Create a new Flask Blueprint
# IMPORTANT: Notice in the routes below, we are adding routes to the
# blueprint object, not the app object.
seasons = Blueprint('seasons', __name__)


@seasons.route('/', methods=["GET"])
def home():
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


@seasons.route('/', methods=["POST"])
def insert():
    data = request.json
    value = data["seasonYear"]
    query = "INSERT INTO Season (seasonYear) VALUES (%s)" % str(value)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_response = make_response()
    the_response.status_code = 200 if cursor.rowcount else 301
    db.get_db().commit()
    return the_response


@seasons.route('/<season>', methods=["GET"])
def other(season):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Tournament WHERE season = %s' %
                   season)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
