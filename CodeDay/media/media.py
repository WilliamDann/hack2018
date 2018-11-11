import reddit
reddit.init()

# General media object
class MediaObject:
    def __init__(self, title, image, link, content=""):
        self.title = title
        self.image = image
        self.link = link
        self.content = content

# Class for data from reddit
class RedditObject(MediaObject):
    def __init__(self, title, image, link, content=""):
        MediaObject.__init__(self, title, image, link, content)
    
    # Get image posts from reddit 
    def getImagePost(subredditName, limit=20, source='hot'):
        posts = reddit.getPosts(subredditName, limit, source)

        returnData = []
        
        for post in posts:
            if post.media:
                returnData.append(MediaObject(post.title, post.media, post.shortlink))
        
        return returnData
    
    # Get text posts from reddit 
    def getTextPost(subredditName, limit=20, source='hot', maxAttempts=1):
        posts = reddit.getPosts(subredditName, limit, source)

        returnData = []
        
        for post in posts:
            if not post.media:
                returnData.append(media.MediaObject(post.title, post.media, post.shortlink))
        
        return returnData

    # Get text posts from reddit 
    def getLinkPost(subredditName, limit=20, source='hot', maxAttempts=1):
        raise NotImplementedError("Not implemented")