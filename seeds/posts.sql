DROP TABLE IF EXISTS accounts CASCADE;
DROP SEQUENCE IF EXISTS accounts_id_seq;

CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;

-- Table Definition
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    username varchar(255) UNIQUE, 
    email varchar(255),
    user_password varchar(255)
);



INSERT INTO accounts (username, email, user_password) VALUES ('gab123', 'gab@gmail.com', 'password123!');
INSERT INTO accounts (username, email, user_password) VALUES ('b0b', 'bob@hotmail.com', 'p123321%');
INSERT INTO accounts (username, email, user_password) VALUES ('user123', 'user123@gmail.com', 'word?35pass');

DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;

-- Table Definition
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    post_content text,
    account_username text,
    CONSTRAINT fk_account FOREIGN KEY (account_username) REFERENCES accounts(username) ON DELETE CASCADE
);

INSERT INTO posts (post_content, account_username) VALUES ('Just In: Penguins found dancing in the streets of Tokyo!  #PenguinParty #TokyoAdventures', 'gab123');
INSERT INTO posts (post_content, account_username) VALUES ('Taylor Swift Drops Surprise Album: Fans in Shock!  #SwiftiesReact #SurpriseAlbum', 'b0b');
INSERT INTO posts (post_content, account_username) VALUES ('Amazing Discovery: Unicorns spotted in the Amazon Rainforest!  #UnicornAdventure #AmazonDiscovery', 'user123');
INSERT INTO posts (post_content, account_username) VALUES ('Exciting News: Just heard that Brazil won the 2026 World Cup!  #Champions #Brazil2026', 'gab123');

