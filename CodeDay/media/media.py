import reddit
reddit.init()

# General media object
class MediaObject:
    def __init__(self, title, image, link, content=""):
        self.title = title
        self.image = image
        self.link = link
        self.content = content

class RedditObject(MediaObject):
    def __init__(self, title, image, link, content=""):
        MediaObject.__init__(self, title, image, link, content)
    
    # Get image posts from reddit 
    def getImagePost(subredditName, limit=20, source='hot', maxAttempts=1):
        posts = reddit.instance.subreddit(subredditName)

        returnData = []
        
        for post in posts:
            if post.media:
                returnData.append(media.MediaObject(post.title, post.media, post.shortlink))
        
        return returnData
