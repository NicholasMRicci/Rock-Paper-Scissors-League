-- This file is to bootstrap a database for the CS3200 project.
-- Create a new database.  You can change the name later.  You'll
-- need this name in the FLASK API file(s),  the AppSmith
-- data source creation.
create database rps_league;

-- Via the Docker Compose file, a special user called webapp will
-- be created in MySQL. We are going to grant that user
-- all privilages to the new database we just created.
-- TODO: If you changed the name of the database above, you need
-- to change it here too.
grant all privileges on rps_league.* to 'webapp' @'%';

flush privileges;

-- Move INTo the database we just created.
-- TODO: If you changed the name of the database above, you need to
-- change it here too.
use rps_league;

-- Put your DDL
CREATE TABLE Spectators (
    userName VARCHAR(50) PRIMARY KEY,
    pwd VARCHAR(50) NOT NULL
);

CREATE TABLE Coaches (
    coachID INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    joinDate DATE NOT NULL,
    birthday DATE NOT NULL,
    phoneNumber VARCHAR(15) NOT NULL
);

CREATE TABLE Teams (
    teamName VARCHAR(50) PRIMARY KEY,
    joinDate DATE NOT NULL,
    streetAddress VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    stateAbbrev VARCHAR(2) NOT NULL,
    zipCode VARCHAR(50) NOT NULL,
    coachID INT,
    CONSTRAINT teamCoach FOREIGN KEY (coachID) REFERENCES Coaches (coachID)
);

CREATE TABLE Players (
    playerID INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    birthday DATE NOT NULL,
    joinDate DATE NOT NULL,
    playerStatus VARCHAR(50) NOT NULL,
    phoneNumber VARCHAR(15) NOT NULL,
    teamName VARCHAR(50) NULL,
    CONSTRAINT playerTeam FOREIGN KEY (teamName) REFERENCES Teams (teamName)
);

CREATE TABLE SpectatorFavPlayers (
    userName VARCHAR(50),
    playerID INT AUTO_INCREMENT,
    CONSTRAINT spectatorKeys PRIMARY KEY (userName, playerID),
    CONSTRAINT favPlayerUser FOREIGN KEY (userName) REFERENCES Spectators (userName) ON DELETE CASCADE,
    CONSTRAINT favPlayers FOREIGN KEY (playerID) REFERENCES Players (playerID) ON DELETE CASCADE
);

CREATE TABLE SpectatorFavTeams (
    userName VARCHAR(50),
    teamName VARCHAR(50),
    CONSTRAINT spectatorKeys2 PRIMARY KEY (userName, teamName),
    CONSTRAINT favTeamUser FOREIGN KEY (userName) REFERENCES Spectators (userName) ON DELETE CASCADE,
    CONSTRAINT favTeams FOREIGN KEY (teamName) REFERENCES Teams (teamName) ON DELETE CASCADE
);

CREATE TABLE Posts (
    postID INT PRIMARY KEY AUTO_INCREMENT,
    userName VARCHAR(50) NOT NULL,
    content text NOT NULL,
    timePosted DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT postUser FOREIGN KEY (userName) REFERENCES Spectators (userName) ON DELETE CASCADE
);

CREATE TABLE Comments (
    commentID INT PRIMARY KEY AUTO_INCREMENT,
    postID INT NOT NULL,
    userName VARCHAR(50) NOT NULL,
    content text NOT NULL,
    timePosted DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT commentUser FOREIGN KEY (username) REFERENCES Spectators (userName) ON DELETE CASCADE,
    CONSTRAINT commentPost FOREIGN KEY (postID) REFERENCES Posts (postID) ON DELETE CASCADE
);

CREATE TABLE Likes (
    userName VARCHAR(50),
    postID INT,
    CONSTRAINT likeKeys PRIMARY KEY (userName, postID),
    CONSTRAINT likeUser FOREIGN KEY (username) REFERENCES Spectators (userName) ON DELETE CASCADE,
    CONSTRAINT likePost FOREIGN KEY (postID) REFERENCES Posts (postID) ON DELETE CASCADE
);

CREATE TABLE Season(seasonYear YEAR PRIMARY KEY);

CREATE TABLE Tournament(
    tournamentID INT PRIMARY KEY AUTO_INCREMENT,
    tournamentName VARCHAR(50) NOT NULL,
    attendance INT NOT NULL,
    streetAddress VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    stateAbbrev VARCHAR(2) NOT NULL,
    zipCode VARCHAR(50) NOT NULL,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    season YEAR NOT NULL,
    CONSTRAINT tournamentSeason FOREIGN KEY (season) REFERENCES Season (seasonYear) ON DELETE CASCADE
);

CREATE TABLE GamesPlayed(
    gameID INT PRIMARY KEY AUTO_INCREMENT,
    player1ID INT NOT NULL,
    player2ID INT NOT NULL,
    team1 VARCHAR(50) NOT NULL,
    team2 VARCHAR(50) NOT NULL,
    player1Throw VARCHAR(8) NOT NULL,
    player2Throw VARCHAR(8) NOT NULL,
    tournamentID INT NOT NULL,
    CONSTRAINT gamePlayer1 FOREIGN KEY (player1ID) REFERENCES Players (playerID) ON DELETE CASCADE,
    CONSTRAINT gamePlayer2 FOREIGN KEY (player2ID) REFERENCES Players (playerID) ON DELETE CASCADE,
    CONSTRAINT gameTeam1 FOREIGN KEY (team1) REFERENCES Teams (teamName) ON DELETE CASCADE,
    CONSTRAINT gameTeam2 FOREIGN KEY (team2) REFERENCES Teams (teamName) ON DELETE CASCADE,
    CONSTRAINT gameTournament FOREIGN KEY (tournamentID) REFERENCES Tournament (tournamentID) ON DELETE CASCADE
);
