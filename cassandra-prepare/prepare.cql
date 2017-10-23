CREATE KEYSPACE users
    WITH REPLICATION = {
        'class' : 'NetworkTopologyStrategy',
        'datacenter1' : 2,
        'DC1' : 2
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

USE users;

INSERT INTO users.users (uid, type, name, contact) VALUES('1', 'email', 'm0sk1t', 'm0sk1t@bk.ru');
INSERT INTO users.users (uid, type, name, contact) VALUES('2', 'email', 'artlitvinov', 'work.litvinov.artem@gmail.com');
INSERT INTO users.users (uid, type, name, contact) VALUES('3', 'email', 'user', 'user@mail.ru');
INSERT INTO users.users (uid, type, name, contact) VALUES('4', 'email', 'user-1', 'user-1@mail.ru');
INSERT INTO users.users (uid, type, name, contact) VALUES('5', 'email', 'user-2', 'user-2@mail.ru');
INSERT INTO users.users (uid, type, name, contact) VALUES('6', 'email', 'user-3', 'user-3@mail.ru');
INSERT INTO users.users (uid, type, name, contact) VALUES('7', 'email', 'user-4', 'user-4@mail.ru');