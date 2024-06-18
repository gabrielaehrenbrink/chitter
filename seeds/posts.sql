DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;


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

