from lib.post_repository import PostRepository
from lib.post import Post

def test_create(db_connection):
    db_connection.seed("seeds/posts.sql") 
    repository = PostRepository(db_connection)
    post = Post(None, 'My content', 'gab123')
    repository.create(post)
    assert post.id == 5
    
def test_get_all_records(db_connection): 
    db_connection.seed("seeds/posts.sql") 
    repository = PostRepository(db_connection) 

    posts = repository.all()
    assert posts == [
        Post(1,'Just In: Penguins found dancing in the streets of Tokyo!  #PenguinParty #TokyoAdventures', 'gab123'),
        Post(2, 'Taylor Swift Drops Surprise Album: Fans in Shock!  #SwiftiesReact #SurpriseAlbum', 'b0b'),
        Post(3, 'Amazing Discovery: Unicorns spotted in the Amazon Rainforest!  #UnicornAdventure #AmazonDiscovery', 'user123'),
        Post(4, 'Exciting News: Just heard that Brazil won the 2026 World Cup!  #Champions #Brazil2026', 'gab123')
        ]


