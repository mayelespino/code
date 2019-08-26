# Notes on Hadoop on Docker

## Images
- [docker pull xpspectre/hadoop-single](https://hub.docker.com/r/xpspectre/hadoop-single/) This worked for me.
```
$docker pull xpspectre/hadoop-single
$docker run -t -i -p 50020:50020 -p 50090:50090 -p 50070:50070 -p 50010:50010 -p 50075:50075 -p 8031:8031 -p 8032:8032 -p 8033:8033 -p 8040:8040 -p 8042:8042 -p 49707:49707 -p 8088:8088 -p 8030:8030 xpspectre/hadoop-single /root/run-hadoop-all.sh
```
## These are the uris
- http://antlet14.local:8088/ - Cluster 
- http://antlet14.local:50070/ - Name node
- http://antlet14.local:50075/ - Data node 1
- http://antlet14.local:8042/ - Resource manager
