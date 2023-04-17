# Some set up for the application

from flask import Flask
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()


def create_app():
    app = Flask(__name__)

    # secret key that will be used for securely signing the session
    # cookie and can be used for any other security related needs by
    # extensions or your application
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'

    # these are for the DB object to be able to connect to MySQL.
    app.config['MYSQL_DATABASE_USER'] = 'webapp'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'ghjf6901'
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    # Change this to your DB name
    app.config['MYSQL_DATABASE_DB'] = 'rps_league'

    # Initialize the database object with the settings above.
    db.init_app(app)

    # Add a default route
    @app.route("/")
    def welcome():
        return "<h1>Welcome to the Rock Paper Scissors League</h1>"

    # Import the various routes
    from src.coaches import coaches
    from src.comments import comments
    from src.likes import likes
    from src.matches import matches
    from src.players import players
    from src.posts import posts
    from src.seasons import seasons
    from src.teams import teams
    from src.users import users
    from src.tournaments import tournaments
    from src.statistics import statistics
    from src.favoriteTeams import favoriteTeams
    from src.favoritePlayers import favoritePlayers

    # Register the routes that we just imported so they can be properly handled
    app.register_blueprint(coaches,       url_prefix='/coaches')
    app.register_blueprint(comments,       url_prefix='/comments')
    app.register_blueprint(likes,       url_prefix='/likes')
    app.register_blueprint(matches,       url_prefix='/matches')
    app.register_blueprint(players,       url_prefix='/players')
    app.register_blueprint(posts,       url_prefix='/posts')
    app.register_blueprint(seasons,       url_prefix='/seasons')
    app.register_blueprint(teams,       url_prefix='/teams')
    app.register_blueprint(tournaments,       url_prefix='/tournaments')
    app.register_blueprint(statistics,       url_prefix='/statistics')
    app.register_blueprint(favoriteTeams,       url_prefix='/favoriteTeams')
    app.register_blueprint(
        favoritePlayers,       url_prefix='/favoritePlayers')

    return app
