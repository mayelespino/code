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

```
CREATE TABLE excelsior.table2 (
key text,
value text,
PRIMARY KEY (key)
);

insert into table (key, value) values ('name', 'amadeus');

COPY table2 (key, value) FROM 'mytable.csv';
COPY table2 (key, value) TO 'table2.csv';
```
# links
https://datastax.github.io/python-driver/getting_started.html
https://docs.datastax.com/en/cql/3.3/cql/cql_reference/copy_r.html
https://www.tutorialspoint.com/cassandra/cassandra_data_model.htm
