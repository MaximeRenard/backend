# Project for ALTEN test
## Projet Back End with Pythhon and Django framework
## Author : Maxime Renard
## Date : 24/09/24 - > 01/10/24

### Utilisation de docker
version
### Langage Python 
Use version 3.12.3
### Use of Framework django
version 5.1.1
### base de données 
PSQL: postgresql

### Launch code 
#### Creation of docker
sudo docker exec -it web_app bash
#root@a604c36ce2b7:/home/docker# ls
#Dockerfile  README.md  docker-compose.yml  requirements.txt  web
sudo docker exec -it web_db bash
root@postgres:/# psql -U postgres
psql (16.4 (Debian 16.4-1.pgdg120+1))
Type "help" for help.
### Tutorial 
#### Create project
django-admin startproject web
python3 manage.py startapp ecommerce
python3 manage.py migrate
python3 manage.py runserver 127.0.0.1:8000
Base de données sqllite3 
#### Inserer modele db
##### ecommerce/models.py
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py showmigrations
### Load
git clone https://github.com/MaximeRenard/backend
git clone git@github.com:MaximeRenard/backend.git
### Version docker
Docker version 27.2.1, build 9e34c9b
### Execute project
sudo docker compose up -d web_db
sudo docker compose up -d web_app
sudo docker ps
Launch postman


