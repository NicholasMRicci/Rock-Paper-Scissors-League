# Rock Paper Scissors League

We created a statistics website for a Rock Paper Scissors League. This product manages statistics for a hypothetical league of rock, paper, scissors matches. In this league, players will face each other in 1 vs. 1 matches consisting of a single throw. Players will belong to variable size teams and those teams are managed by one coach each. Our users will consist of owners, coaches, and spectators who have different levels of control over the data. All users will have access to a suite of tools to view different statistics on the players, coaches, and teams while spectators can pick out their favorite players and teams. The goal of this website is to keep all users informed about the happenings of this hypothetical league in an easy to digest manner.

Video: [YouTube Link](https://www.youtube.com/watch?v=OqJ1IphEBxM)

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 
