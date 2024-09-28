FROM ubuntu:22.04


FROM python:3.12
# Label
LABEL maintaner = "maxime.renard@protonmail.com"
LABEL version="1.0"
LABEL readme="Projet Backend Python/Django"

# Environment of file
RUN mkdir /home/docker
WORKDIR /home/docker

# COPY file   
COPY requirements.txt /home/docker
COPY web/ /home/docker

# Install app
RUN pip3 install -r requirements.txt
RUN python3 -m pip install --upgrade Pillow==10.4.0 --break-system-packages



