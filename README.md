# Project for ALTEN test
## Projet Back End
## Author : Maxime Renard


### Utilisation de docker
### Experience with Langage Python 
Use version 3.12.3
### Use of Framework django
version 5.1.1
### base de données 
PSQL: postgresql

### Launch code 
#### 14/09/2024 : First version 
sudo docker exec -it django-web-web-1 bash
#root@a604c36ce2b7:/home/docker# ls
#Dockerfile  README.md  docker-compose.yml  requirements.txt  web
sudo docker exec -it django-web-db-1 bash
root@postgres:/# psql -U postgres
psql (16.4 (Debian 16.4-1.pgdg120+1))
Type "help" for help.
### Architecture
#### Commande creation django project
django-admin startproject web
Dans docker-compose commande
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
Essai base de données 
PSQL perte temps
python3 manage.py startapp ecommerce
#### Inserer modele db
sudo docker exec -it django-web-web-1 bash
python3 manage.py makemigrations
python3 manage.py migrate
Shell django
python3 manage.py shell
### Launch program
git 
# Version docker
sudo docker compose up

# Date : 11/09/24 - > 19/09/24
