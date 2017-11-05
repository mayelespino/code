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

# links
https://datastax.github.io/python-driver/getting_started.html
https://docs.datastax.com/en/cql/3.3/cql/cql_reference/copy_r.html
https://www.tutorialspoint.com/cassandra/cassandra_data_model.htm
- [datastax getting started](https://datastax.github.io/python-driver/getting_started.html)
