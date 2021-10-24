# Notes on cassandra


## creating a keyspace and table
- [create keyspace](https://docs.datastax.com/en/cql/3.1/cql/cql_using/example_creating_ks_t.html)
```
cqlsh> CREATE KEYSPACE demodb WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 3 };
```
- [create a table](https://docs.datastax.com/en/cql/3.1/cql/cql_using/create_table_t.html)
```
CREATE TABLE users (
  user_name varchar,
  password varchar,
  gender varchar,
  session_token varchar,
  state varchar,
  birth_year bigint,
  PRIMARY KEY (user_name));
```

## running the docker container exposing the ports correctly
```
docker run --name cassandra -p 9042:9042 -p 9160:9160 -d cassandra
```

## running cqlsh
```
docker exec -it cassandra bash
```
## some cqlsh usefull commands
```
DESCRIBE commands    Example    Description
DESCRIBE CLUSTER    DESCRIBE CLUSTER;    Output information about the connected Cassandra cluster. Cluster name, partitioner, and snitch are output. For non-system keyspace, the endpoint-range ownership information is also shown.
DESCRIBE KEYSPACES        Output a list of all keyspace names.
DESCRIBE KEYSPACE <keyspace_name>    DESCRIBE KEYSPACE cycling;    Output CQL commands for the given keyspace. These CQL commands can be used to recreate the keyspace and tables.
DESCRIBE [FULL] SCHEMA         Output CQL commands for entire non-system keyspace and table schema. Use the FULL option to also include system keyspaces.
DESCRIBE TABLES         Output all tables in the current keyspace, or in all keyspaces if there is not current keyspace.
DESCRIBE TABLE <table_name>    DESCRIBE TABLE upcoming_calendar;    Output CQL commands for the given table. This CQL command can be used to recreate the table.
DESCRIBE INDEX <index_name>    DESCRIBE INDEX team_entry;    Output CQL command for the given index. This CQL command can be used to recreate the index.
DESCRIBE TYPES         Output list of all user-defined types in the current keyspace.
DESCRIBE TYPE <type_name>    DESCRIBE TYPE basic_info;    Output CQL command for the given user-defined type. This CQL command can be used to recreate the index.
```
# Notes
- there is a ~/code/cassandra directory which has file you may be interested in, for example some *.cql files which can be run from cqlsh
## 
# links
https://datastax.github.io/python-driver/getting_started.html
https://docs.datastax.com/en/cql/3.3/cql/cql_reference/copy_r.html
https://www.tutorialspoint.com/cassandra/cassandra_data_model.htm
- [datastax getting started](https://datastax.github.io/python-driver/getting_started.html)
