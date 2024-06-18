DROP TABLE IF EXISTS accounts CASCADE;
DROP SEQUENCE IF EXISTS accounts_id_seq;

CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;


CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    username varchar(255) UNIQUE, 
    email varchar(255),
    user_password varchar(255)
);



INSERT INTO accounts (username, email, user_password) VALUES ('gab123', 'gab@gmail.com', 'password123!');
INSERT INTO accounts (username, email, user_password) VALUES ('b0b', 'bob@hotmail.com', 'p123321%');
INSERT INTO accounts (username, email, user_password) VALUES ('user123', 'user123@gmail.com', 'word?35pass');