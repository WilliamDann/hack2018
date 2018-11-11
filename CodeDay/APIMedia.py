from RedditObject import RedditObject as ro
from news import NewsParser

increaseRate = 10

class MediaSet:
    def __init__(self, quote, quoteurl, imageurl, imagetitle, imageposturl, newsurl, newstitle, newsdesc, newsimg):
        self.quote = quote
        self.quoteurl = quoteurl

        self.imageurl = imageurl
        self.imagetitle = imagetitle
        self.imageposturl = imageposturl

        self.newsurl = newsurl
        self.newstitle = newstitle
        self.newsdesc = newsdesc
        self.newsimg = newsimg
    
    def getJSONFormatted(self):
        return {
            "quote": {
                "text": self.quote,
                "url": self.quoteurl
            },
            "image": {
                "image": self.imageurl,
                "title": self.imagetitle,
                "url": self.imageposturl
            },
            "news": {
                "url": self.newsurl,
                "title": self.newstitle,
                "description": self.newsdesc,
                "image": self.newsimg
            }
        }

def agregate(subredditimg, subredditquote, subredditnews):
    count = 10
    imgpost = ro.getImagePost(subredditimg,count)
    while(len(imgpost) == 0):
        print("ImgPostCount |", count)
        count+=increaseRate
        imgpost = ro.getImagePost(subredditimg,count)
    

    count = 10
    quotepost = ro.getTextPost(subredditquote,count) 
    while(len(quotepost)==0):
        print("QuotePostCount |", count)
        count+=increaseRate
        quotepost = ro.getTextPost(subredditquote,count)
    
    count = 10
    newsPost = ro.getLinkPost(subredditnews, count)
    while(len(quotepost)==0):
        print("NewPostCountcls |", count)
        count+=increaseRate
        newsPost = ro.getLinkPost(subredditnews, count)
    
    newsDesc, newsImage = None, None
    if len(newsPost) > 0:     
        newsDesc, newsImage = NewsParser.parseArticle(newsPost[0].content)

    return MediaSet(quotepost[0].title, quotepost[0].link,
                    imgpost[0].image, imgpost[0].title,  imgpost[0].link,
                    newsPost[0].content, newsPost[0].title, newsDesc, newsImage)

