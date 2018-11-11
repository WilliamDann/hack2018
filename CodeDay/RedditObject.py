from media import MediaObject
import reddit

reddit.init()

listOfImgHosts = ['imgur', 'gfycat', 'gyazo', 'i.redd.it']

# Determine if a link is an image
def isImage(post):
    for host in listOfImgHosts:
        if host in post.url:
            return True
    
    return False

# Class for data from reddit
class RedditObject(MediaObject):
    def __init__(self, title, image, link, content=""):
        MediaObject.__init__(self, title, image, link, content)
    

    # Determines if a post is 
    def filterPost(postData, allowVideo=False, allowStickied=False):
        # Disallow stickied posts
        if postData.stickied and not allowStickied:
            return False

        if postData.is_video and not allowVideo:
            return False
        
        return True

    # Get image posts from reddit 
    def getImagePost(subredditName, limit=1, source='hot'):
        posts = reddit.getPosts(subredditName, limit, source)

        returnData = []
        
        for post in posts:
            if isImage(post) and RedditObject.filterPost(post):
                returnData.append(MediaObject(post.title, post.url, post.shortlink, None))
        
        return returnData
    
    # Get text posts from reddit 
    def getTextPost(subredditName, limit=1, source='hot', maxAttempts=1):
        posts = reddit.getPosts(subredditName, limit, source)

        returnData = []
        
        for post in posts:
            if post.is_self and RedditObject.filterPost(post):
                returnData.append(MediaObject(post.title, post.media, post.shortlink, post.selftext))
        
        return returnData

    # Get text posts from reddit 
    def getLinkPost(subredditName, limit=1, source='hot', maxAttempts=1):
        posts = reddit.getPosts(subredditName, limit, source)

        returnData = []
        
        for post in posts:
            if (not isImage(post) and not post.is_self) and RedditObject.filterPost(post):
                returnData.append(MediaObject(post.title, post.media, post.shortlink, post.url))
        
        return returnData