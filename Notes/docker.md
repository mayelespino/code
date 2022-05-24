# how to run a container with a local path mounted inside it
- [bind mounts](https://docs.docker.com/storage/bind-mounts/)

```
sudo docker run -d -it --name con --mount type=bind,source=/home/mayel/GIT,target=/home 6b073e433c0b
```

# How to ssh in to a running container
- [SSH into Running Docker Containers with docker exec](https://adamtheautomator.com/ssh-into-docker-container/)

```
sudo docker exec -it con01 /bin/bash
```

