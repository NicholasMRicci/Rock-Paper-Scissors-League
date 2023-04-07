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
CREATE Table Players (
    PlayerID int,
    First_Name varchar(50),
    Last_Name varchar(50),
    Birthday date,
    joinDate date,
    playerStatus varchar(50),
    phoneNumber varchar(15),
    teamName varchar(50),
);