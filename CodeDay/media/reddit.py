import praw
import media

instance = None

# Initilize a connection with reddit
def init():
    global instance
    instance = praw.Reddit(
        client_id="nDBkcRjDgJIqIQ",
        client_secret="I6O4uV0jRaNkOmVjD4bzAqS3Iq0",
        user_agent="makemehappy bot",
        username="makemehappybot",
        password="makemehappybot"
    )

# Get the posts from a subreddit
def getPosts(subredditName, limit=20, source='hot'):
    if instance is None:
        raise Exception("Reddit instance not initilized! call init()")

    subredditItem = instance.subreddit(subredditName)
    
    data = None
    returnData = []

    # TODO add all data sources
    if (source == 'hot'):
        data = subredditItem.hot(limit=limit)
    elif (source == 'top'):
        data = subredditItem.top(limit=limit)

    for post in data:
        returnData.append(media.MediaObject(post.title, post.media, post.shortlink))
    
    return returnData