#!/bin/sh
#
if [ -z "$1" ]
then
    echo "pass in a contaner NAME, not id."
    sudo docker ps
    exit 0
fi
sudo docker exec -it "$1" /bin/bash
