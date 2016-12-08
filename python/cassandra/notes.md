# Notes on cassandra


## creating a keyspace and table
```
CREATE KEYSPACE Excelsior WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };


CREATE TABLE Excelsior.mytable (
myid uuid,
mykey text,
myvalue text,
PRIMARY KEY ((myid), mykey)
);

CREATE INDEX ON Excelsior.users (mykey);

insert into mytable (myid, mykey, myvalue) values (now(), 'name', 'amadeus');     
```