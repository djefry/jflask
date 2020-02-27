# JFlask
## Basic Event Messaging with Flask, Celery, SQLAlchemy and Postgres run in Docker
##
## Requirements:
#### - Docker
#### - Docker-Compose
#### - PostgreSQL 11.7
##
## How to use:
#### To Serving With Docker :
#### - You need to install docker and docker-compose in your machine
#### - sudo docker-compose build
#### - sudo docker-compose up
#### - visit your localhost:80
#### NOTE : If you have used postgres database in your docker container before, clean it. Back up and remove all the tables.
####
#### To Testing :
#### You need to have PostgreSQL installed on your machine
#### From inside directory that you save this project
#### - Make virtual environment for this project and activate it
#### - run "python setup.py install" in your shell
#### - run "pytest" in your shell
#### 
#### To Run Locally :
#### You need to have PostgreSQL, Redis installed on your machine
#### From inside directory that you save this project
#### - Make virtual environment for this project and activate it
#### - run "python setup.py install" in your shell
#### - Open run.py change port to 8000, and change database url password and redis url
#### - run "python run.py", run celery beat and worker
#### - visit your localhost:8000