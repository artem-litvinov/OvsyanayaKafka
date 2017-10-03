CREATE KEYSPACE users
    WITH REPLICATION = {
        'class' : 'SimpleStrategy',
        'replication_factor' : 1
    };

CREATE TABLE users.users (
    uid text PRIMARY KEY,
    type text,
    name text,
    contact text
);

CREATE TABLE users.messages (
    mid text PRIMARY KEY,
    uid text,
    date text,
    text text,
    status text
);