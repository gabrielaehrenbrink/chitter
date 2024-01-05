from lib.post import Post


class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["post_content"], row["account_username"])
            posts.append(item)
        return posts


    def create(self, post):
        rows = self._connection.execute('INSERT INTO posts (post_content, account_username) VALUES (%s, %s) RETURNING id', (post.post_content, post.account_username))
        post.id = rows[0]['id']
        return None


