#!/bin/sh
sudo docker run -d -it --name pydev --mount type=bind,source="/home/mayel/GIT",target=/home python:latest
sudo docker run -d -it --name rustdev --mount type=bind,source="/home/mayel/GIT",target=/home rust:latest
sudo docker run -d -it --name godev --mount type=bind,source="/home/mayel/GIT",target=/home golang:latest
sudo docker run -d -it --name gccdev --mount type=bind,source="/home/mayel/GIT",target=/home :latest

echo "Now running:"
sudo docker ps
#
# links
# https://docs.docker.com/storage/bind-mounts/
