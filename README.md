# Project for ALTEN test
## Projet Back End with Python with Django framework
## Author : Maxime Renard


### Containerisation with docker
Docker version 27.3.1, build ce12230
Ubuntu 22.04
### Langage Python 
Use version 3.12.3
### Use of Framework django
version 5.1.1
### base de données 
PSQL: postgresql:16

### Launch code 
#### 14/09/2024 : Creation of docker
sudo docker exec -it web_app bash
#root@a604c36ce2b7:/home/docker# ls
#Dockerfile  README.md  docker-compose.yml  requirements.txt  web
sudo docker exec -it web_db bash
root@postgres:/# psql -U postgres
psql (16.4 (Debian 16.4-1.pgdg120+1))
Type "help" for help.
### Architecture
#### Commande creation django project
##### Create project
django-admin startproject web
##### Create application
python3 manage.py startapp ecommerce
python3 manage.py migrate
python3 manage.py runserver 127.0.0.1:8000
Base de données sqlite3 

####  Model db and function
##### ecommerce/models.py
Class of product
##### Migrations Result of Migrate
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py showmigrations
##### Pictures 
Instance of default pictures
##### Template
html code for whelcome page
##### Assets
Example of product : Create and models of update product

##### ecommerce/views.py
Function for manage store
GET product
POST product
DELETE product
PATCH specific product
#### Postman 
Result of Postman test of api ecommerce


### Load program
git clone https://github.com/MaximeRenard/backend
or 
git clone git@github.com:MaximeRenard/backend.git
### Version docker
Docker version 27.2.1, build 9e34c9b
### Execute project
sudo docker compose up -d web_db
sudo docker compose up -d web_app
sudo docker ps
Launch postman

# Date : 24/09/24 - > 01/10/24
