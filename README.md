# Project for ALTEN test
## Projet Back End with Python with Django framework
## Author : Maxime Renard
## Date : 24/09/24 - > 01/10/24

### Containerisation with docker
Docker version 27.3.1, build ce12230\
System : Ubuntu 22.04
### Langage Python 
Use version 3.12.3
### Use of Framework django
version 5.1.1
### base de données 
Default django.db.backends.sqlite3 \
Try PSQL: postgresql:16\
Container postgres:16.4 application web_db install\
Work if connect database in local computer\
Connect with psycopg2 module\
Example in web/web/settings.py "psql"


### Architecture
#### Creation order django project
##### Create project
django-admin startproject web
##### Create application
python3 manage.py startapp ecommerce\
python3 manage.py migrate\
python3 manage.py runserver 127.0.0.1:8000\
database sqlite3 (configuration in web/web/settings.py ) 

####  Model db and function
##### ecommerce/models.py
Class of product
##### Migrations Result of Migrates
python3 manage.py makemigrations\
python3 manage.py migrate\
python manage.py showmigrations\
Database in web/db.sqlite3
##### Pictures 
Instance of default pictures
##### Template
html code for whelcome page
##### Assets
Example of product : Create and models of update product

##### ecommerce/views.py
Function for manage store\
GET product\
GET specific product\
POST product\
DELETE product\
PATCH specific product\ 
#### Postman 
Result of Postman test of api ecommerce\
Request_Postman : History of request\
Request_project.png : Screen capture of terminal\
REST API_ecommerce_MaximeRenard_basics- CRUD, test & variable.postman_collection.json \
Save collection of Postman Test

### Load program
git clone https://github.com/MaximeRenard/backend.git \
or \
git clone git@github.com:MaximeRenard/backend.git \
### Version docker
Docker version 27.2.1, build 9e34c9b
### Execute project
Specification of configuration in DockerFile and \
docker-compose.yml
#### Container
sudo docker compose up -d web_db \
sudo docker compose up -d web_app \ 
#### All
sudo docker compose up\
In Postman directory Example of launch application 
#### See containers
sudo docker ps \
sudo docker images \
Launch postman for test\
postman --disable-gpu v11.7 on ubuntu 24.04.1 LTS
#### Exec specific container
sudo docker exec -it web_app bash<\br> 
#root@a604c36ce2b7:/home/docker# ls<\br\> 
#Dockerfile  README.md  docker-compose.yml  requirements.txt  web <\br>  
Container Psql: <\br> 
sudo docker exec -it [726bbd49d667]_web_db bash<br\>   
root@postgres:/# psql -U postgres<br\> 
psql (16.4 (Debian 16.4-1.pgdg120+1))<br\> 
Recall : use sqlite in default
