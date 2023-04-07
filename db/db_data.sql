USE rps_league;

INSERT INTO Spectators (userName, pwd) VALUES ('brent123', '1234');
INSERT INTO Spectators (userName, pwd) VALUES ('taylorlol', 'abc');
INSERT INTO Spectators (userName, pwd) VALUES ('jamesxd', 'rps');

INSERT Coaches (coachID, firstName, lastName, joinDate, birthday, phoneNumber)
    VALUES (1, 'Phil', 'Buster', '2015-07-28', '2000-9-12', '617-213-1382');
INSERT Coaches (coachID, firstName, lastName, joinDate, birthday, phoneNumber)
    VALUES (2, 'Susan', 'Anthony', '2021-01-03', '1997-12-12', '617-362-5124');
INSERT Coaches (coachID, firstName, lastName, joinDate, birthday, phoneNumber)
    VALUES (3, 'Phil', 'Buster', '2015-07-28', '2000-9-12', '617-967-421');
INSERT INTO mytable(coachID,firstName,lastName,joinDate,birthday,phoneNumber) 
    VALUES (4, 'Marcile', 'Britcher', '2018-04-12', '2004-10-12', '456-561-9362');

-- tournamnet data
INSERT INTO Tournament (tournamentID,tournamentName,attendance,streetAddress,city,stateAbbrev,zipCode,startDate,endDate,season) VALUES (1,'Tournament1',122,'54783 Heath Lane','Killeen','TX',76544,'2016-04-16','2016-04-25',2017);
INSERT INTO Tournament (tournamentID,tournamentName,attendance,streetAddress,city,stateAbbrev,zipCode,startDate,endDate,season) VALUES (2,'Tournament2',48,'1224 Sloan Park','Washington','DC',20535,'2020-05-21','2020-05-30',2015);
INSERT INTO Tournament (tournamentID,tournamentName,attendance,streetAddress,city,stateAbbrev,zipCode,startDate,endDate,season) VALUES (3,'Tournament3',278,'55 Troy Hill','Minneapolis','MN',55487,'2018-09-02','2018-09-09',2017);
INSERT INTO Tournament (tournamentID,tournamentName,attendance,streetAddress,city,stateAbbrev,zipCode,startDate,endDate,season) VALUES (4,'Tournament4',242,'246 Dunning Circle','New York City','NY',10024,'2020-11-20','2020-11-28',2018);

-- player data
INSERT INTO Players(playerID,firstName,lastName,birthday,joinDate,playerStatus,phoneNumber,teamName) VALUES (1,'Guthry','Vedeniktov','1999-04-15','2015-03-25','active','511-202-6048','Team9');
INSERT INTO Players(playerID,firstName,lastName,birthday,joinDate,playerStatus,phoneNumber,teamName) VALUES (2,'Harwell','Basnett','2001-11-09','2015-01-29','active','539-971-5807','Team2');
INSERT INTO Players(playerID,firstName,lastName,birthday,joinDate,playerStatus,phoneNumber,teamName) VALUES (3,'Teddie','Whatmough','1997-11-07','2017-04-16','doubtful','513-611-0064','Team2');
INSERT INTO Players(playerID,firstName,lastName,birthday,joinDate,playerStatus,phoneNumber,teamName) VALUES (4,'Benito','Dinkin','1996-10-27','2017-06-15','doubtful','687-303-3546','Team2');

-- team data
INSERT INTO Teams(teamName,joindate,streetAddress,city,stateAbbrev,zipCode,coachID) VALUES ('Team9','2018-12-19','173 Rieder Terrace','Brockton','MA',02305,3);
INSERT INTO Teams(teamName,joindate,streetAddress,city,stateAbbrev,zipCode,coachID) VALUES ('Team8','2017-06-19','135 Cascade Avenue','Shawnee Mission','KS',66205,3);
INSERT INTO Teams(teamName,joindate,streetAddress,city,stateAbbrev,zipCode,coachID) VALUES ('Team2','2018-11-17','7736 Mockingbird Center','Virginia Beach','VA',23464,1);
INSERT INTO Teams(teamName,joindate,streetAddress,city,stateAbbrev,zipCode,coachID) VALUES ('Team1','2022-06-11','57 Buhler Way','Waco','TX',76796,2);

-- spectator fave teams
-- spectator fave players
-- posts 
-- comments 
-- likes
-- season
-- games played