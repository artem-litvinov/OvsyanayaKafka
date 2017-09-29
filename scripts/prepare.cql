CREATE KEYSPACE users
    WITH REPLICATION = {
        'class' : 'SimpleStrategy',
        'replication_factor' : 1
    };

CREATE TABLE users (
    user_id text PRIMARY KEY,
    type text,
    contact text
);