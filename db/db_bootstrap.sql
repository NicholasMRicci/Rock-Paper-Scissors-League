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

-- Move into the database we just created.
-- TODO: If you changed the name of the database above, you need to
-- change it here too. 
use rps_league;

-- Put your DDL 
CREATE TABLE Players (
    playerID int,
    firstName varchar(50),
    lastName varchar(50),
    birthday date,
    joinDate date,
    playerStatus varchar(50),
    phoneNumber varchar(15),
    teamName varchar(50)
);

CREATE TABLE Teams (
    teamName varchar(50),
    joinDate date,
    streetAddress varchar(50),
    city varchar(50),
    stateAbbrev varchar(2),
    zipCode varchar(50)
);

CREATE TABLE Spectators (userName varchar(50), pwd varchar(50));

CREATE TABLE SpectatorFavPlayers (userName varchar(50), playerID int);

CREATE TABLE SpectatorFavTeams (userName varchar(50), teamName varchar(50));

CREATE TABLE Coaches (
    coachID int,
    firstName varchar(50),
    lastName varchar(50),
    joinDate date,
    birthday date,
    phoneNumber varchar(15)
);

CREATE TABLE Posts (
    postID int,
    userName varchar(50),
    content text,
    timePosted datetime
);

CREATE TABLE Comments (
    commentID int,
    postID int,
    userName varchar(50),
    content text,
    timePosted datetime
);

CREATE TABLE Likes (userName varchar(50), postID int);

CREATE TABLE GamesPlayed(
    gameID int,
    player1ID int,
    player2ID int,
    team1 varchar(50),
    team2 varchar(50),
    player1Throw varchar(8),
    player2Throw varchar(8),
    tournament int,
);

CREATE TABLE Tournament(
    tournamentID int,
    name varchar(50),
    attendance int,
    streetAddress varchar(50),
    city varchar(50),
    stateAbbrev varchar(2),
    zipCode varchar(50),
    startDate date,
    endDate date,
    season year,
);

CREATE TABLE Season(yearPlayed year);