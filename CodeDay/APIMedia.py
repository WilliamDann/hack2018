from RedditObject import RedditObject

class MediaSet:
    def __init__(self, quote, imageurl, imagetitle, newsurl, newstitle):
        self.quote = quote
        self.imageurl = imageurl
        self.imagetitle = imagetitle
        self.newsurl = newsurl
        self.newstitle = newstitle

@staticmethod
def agregate(subredditimg, subredditquote, subredditnews):
    imgpost = ro.RedditObject.getImagePost(subredditimg)#TODO forloop to check for images in here
    quotepost = ro.RedditObject.getTextPost(subredditquote) #TODO forloop to check for quotes in here
    newsPost = ro.RedditObject.getLinkPost(subredditnews)#TODO forloop to check for images in here

    return MediaSet(quotepost[0].content, 
                    imgpost[0].image, imgpost[0].link, 
                    newsPost[0].content, newsPost[0].title)