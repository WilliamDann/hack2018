from RedditObject import RedditObject as ro
from news import NewsParser

increaseRate = 10

class MediaSet:
    def __init__(self, quote, imageurl, imagetitle, newsurl, newstitle, newsdesc):
        self.quote = quote
        self.imageurl = imageurl
        self.imagetitle = imagetitle
        self.newsurl = newsurl
        self.newstitle = newstitle
        self.newsdesc = newsdesc
    
    def getJSONFormatted(self):
        return {
            "quote":self.quote,
            "imageurl":self.imageurl,
            "imagetitle":self.imagetitle,
            "newsurl":self.newsurl,
            "newstitle":self.newstitle,
            "newsdesc":self.newsdesc
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

    newsDesc = NewsParser.parseArticle(newsPost[0].content)

    return MediaSet(quotepost[0].title, 
                    imgpost[0].image, imgpost[0].title, 
                    newsPost[0].content, newsPost[0].title, newsDesc)

