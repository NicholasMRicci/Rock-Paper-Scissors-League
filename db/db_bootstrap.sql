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
    teamName VARCHAR(50),
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
    CONSTRAINT favTeams FOREIGN KEY (teamName) REFERENCES Teams (teamName)  ON DELETE CASCADE
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

-- EXAMPLE DATA

-- spectator data
INSERT INTO Spectators (userName, pwd) VALUES ('brent123', '1234');
INSERT INTO Spectators (userName, pwd) VALUES ('taylorlol', 'abc');
INSERT INTO Spectators (userName, pwd) VALUES ('jamesxd', 'rps');

-- coach data
INSERT INTO Coaches (coachID, firstName, lastName, joinDate, birthday, phoneNumber)
    VALUES (1, 'Phil', 'Buster', '2015-07-28', '2000-9-12', '617-213-1382');
INSERT INTO Coaches (coachID, firstName, lastName, joinDate, birthday, phoneNumber)
    VALUES (2, 'Susan', 'Anthony', '2021-01-03', '1997-12-12', '617-362-5124');
INSERT INTO Coaches (coachID, firstName, lastName, joinDate, birthday, phoneNumber)
    VALUES (3, 'Phil', 'Buster', '2015-07-28', '2000-9-12', '617-967-421');
INSERT INTO Coaches (coachID,firstName,lastName,joinDate,birthday,phoneNumber)
    VALUES (4, 'Marcile', 'Britcher', '2018-04-12', '2004-10-12', '456-561-9362');

-- season data
INSERT INTO Season(seasonYear) VALUES (2015);
INSERT INTO Season(seasonYear) VALUES (2016);
INSERT INTO Season(seasonYear) VALUES (2017);
INSERT INTO Season(seasonYear) VALUES (2018);

-- tournament data
INSERT INTO Tournament (tournamentID,tournamentName,attendance,streetAddress,city,stateAbbrev,zipCode,startDate,endDate,season) VALUES (1,'Tournament1',122,'54783 Heath Lane','Killeen','TX',76544,'2016-04-16','2016-04-25',2017);
INSERT INTO Tournament (tournamentID,tournamentName,attendance,streetAddress,city,stateAbbrev,zipCode,startDate,endDate,season) VALUES (2,'Tournament2',48,'1224 Sloan Park','Washington','DC',20535,'2020-05-21','2020-05-30',2015);
INSERT INTO Tournament (tournamentID,tournamentName,attendance,streetAddress,city,stateAbbrev,zipCode,startDate,endDate,season) VALUES (3,'Tournament3',278,'55 Troy Hill','Minneapolis','MN',55487,'2018-09-02','2018-09-09',2017);
INSERT INTO Tournament (tournamentID,tournamentName,attendance,streetAddress,city,stateAbbrev,zipCode,startDate,endDate,season) VALUES (4,'Tournament4',242,'246 Dunning Circle','New York City','NY',10024,'2020-11-20','2020-11-28',2018);

-- team data
INSERT INTO Teams(teamName,joindate,streetAddress,city,stateAbbrev,zipCode,coachID) VALUES ('Team9','2018-12-19','173 Rieder Terrace','Brockton','MA',02305,3);
INSERT INTO Teams(teamName,joindate,streetAddress,city,stateAbbrev,zipCode,coachID) VALUES ('Team8','2017-06-19','135 Cascade Avenue','Shawnee Mission','KS',66205,3);
INSERT INTO Teams(teamName,joindate,streetAddress,city,stateAbbrev,zipCode,coachID) VALUES ('Team2','2018-11-17','7736 Mockingbird Center','Virginia Beach','VA',23464,1);
INSERT INTO Teams(teamName,joindate,streetAddress,city,stateAbbrev,zipCode,coachID) VALUES ('Team1','2022-06-11','57 Buhler Way','Waco','TX',76796,2);

-- player data
INSERT INTO Players(playerID,firstName,lastName,birthday,joinDate,playerStatus,phoneNumber,teamName) VALUES (1,'Guthry','Vedeniktov','1999-04-15','2015-03-25','active','511-202-6048','Team9');
INSERT INTO Players(playerID,firstName,lastName,birthday,joinDate,playerStatus,phoneNumber,teamName) VALUES (2,'Harwell','Basnett','2001-11-09','2015-01-29','active','539-971-5807','Team2');
INSERT INTO Players(playerID,firstName,lastName,birthday,joinDate,playerStatus,phoneNumber,teamName) VALUES (3,'Teddie','Whatmough','1997-11-07','2017-04-16','doubtful','513-611-0064','Team2');
INSERT INTO Players(playerID,firstName,lastName,birthday,joinDate,playerStatus,phoneNumber,teamName) VALUES (4,'Benito','Dinkin','1996-10-27','2017-06-15','doubtful','687-303-3546','Team2');

-- spectator fave teams
INSERT INTO SpectatorFavTeams(userName,teamName) VALUES ('brent123','Team2');
INSERT INTO SpectatorFavTeams(userName,teamName) VALUES ('taylorlol','Team2');
INSERT INTO SpectatorFavTeams(userName,teamName) VALUES ('jamesxd','Team9');
INSERT INTO SpectatorFavTeams(userName,teamName) VALUES ('jamesxd','Team2');
-- spectator fave players
INSERT INTO SpectatorFavPlayers(userName,playerID) VALUES ('taylorlol','2');
INSERT INTO SpectatorFavPlayers(userName,playerID) VALUES ('brent123','1');
INSERT INTO SpectatorFavPlayers(userName,playerID) VALUES ('jamesxd','2');
INSERT INTO SpectatorFavPlayers(userName,playerID) VALUES ('brent123','3');
-- posts
INSERT INTO Posts(postID,userName,content,timePosted) VALUES (1,'jamesxd','This is so crazy','2023-01-26 03:04:44');
INSERT INTO Posts(postID,userName,content,timePosted) VALUES (2,'taylorlol','I can not wait to see how this turns out.','2022-01-16 07:27:26');
INSERT INTO Posts(postID,userName,content,timePosted) VALUES (3,'taylorlol','Pretend this is a post.','2023-02-10 09:29:41');
INSERT INTO Posts(postID,userName,content,timePosted) VALUES (4,'brent123','This is so crazy','2021-11-17 17:38:01');
-- comments
INSERT INTO Comments(commentID,postID,username,content,timePosted) VALUES (1,1,'taylorlol','I agree!','2022-11-09 06:00:03');
INSERT INTO Comments(commentID,postID,username,content,timePosted) VALUES (2,1,'brent123','What is going on?','2022-11-27 07:27:56');
INSERT INTO Comments(commentID,postID,username,content,timePosted) VALUES (3,1,'jamesxd','That is so controversial','2022-03-31 22:14:23');
INSERT INTO Comments(commentID,postID,username,content,timePosted) VALUES (4,4,'brent123','That is so controversial','2022-09-23 05:04:01');
-- likes
INSERT INTO Likes(userName, postID) VALUES ('taylorlol', 1);
INSERT INTO Likes(userName, postID) VALUES ('jamesxd', 2);
INSERT INTO Likes(userName, postID) VALUES ('taylorlol', 4);
INSERT INTO Likes(userName, postID) VALUES ('brent123', 1);

-- games played
INSERT INTO GamesPlayed(gameId,player1ID,player2ID,team1,team2,player1Throw,player2Throw,tournamentID) VALUES (1,3,4,'Team2','Team8','Scissors','Rock',1);
INSERT INTO GamesPlayed(gameId,player1ID,player2ID,team1,team2,player1Throw,player2Throw,tournamentID) VALUES (2,2,4,'Team2','Team9','Rock','Paper',4);
INSERT INTO GamesPlayed(gameId,player1ID,player2ID,team1,team2,player1Throw,player2Throw,tournamentID) VALUES (3,1,4,'Team2','Team9','Scissors','Scissors',4);
INSERT INTO GamesPlayed(gameId,player1ID,player2ID,team1,team2,player1Throw,player2Throw,tournamentID) VALUES (4,2,2,'Team2','Team9','Rock','Scissors',3);
