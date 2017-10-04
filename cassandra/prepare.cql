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

INSERT INTO users.users (uid, type, name, contact) VALUES("1", "email", "m0sk1t", "m0sk1t@bk.ru");
INSERT INTO users.users (uid, type, name, contact) VALUES("2", "email", "artlitvinov", "work.litvinov.artem@gmail.com");