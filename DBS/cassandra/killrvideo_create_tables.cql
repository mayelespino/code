CREATE KEYSPACE killrvideo WITH REPLICATION = {
    'class': 'SimpleStrategy',
    'replication_factor' : 1
};

use killrvideo;

CREATE TABLE table1 (
    column1 TEXT,
    column2 TEXT,
    column3 INT,
    PRIMARY KEY (column1)
);

CREATE TABLE users (
    user_id UUID,
    first_name TEXT,
    last_name TEXT,
    PRIMARY KEY (user_id)
);
