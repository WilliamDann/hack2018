from RedditObject import RedditObject as ro
from news import NewsParser
from random import randint
import re

increaseRate = 10
newsSites = ["cnn.com", "bbc.com", "msnbc.com", "nytimes.com", "wsj.com", "foxnews.com", "huffingtonpost.com", "washingtonpost.com", "latimes.com", "reuters.com", "abcnews.go.com", "usatoday.com", "bloomberg.com", "nbcnews.com", "dailymail.co.uk", "theguardian.com", "timesofindia.indiatimes.com", "news.com.au", "yahoo.com", "news.google.com"]

class MediaSet:
    def __init__(self, quote, quoteurl, imageurl, imagetitle, imageposturl, newsurl, newstitle, newsdesc, newsimg, newslink):
        self.quote = quote
        self.quoteurl = quoteurl

        self.imageurl = imageurl
        self.imagetitle = imagetitle
        self.imageposturl = imageposturl

        self.newsurl = newsurl
        self.newstitle = newstitle
        self.newsdesc = newsdesc
        self.newsimg = newsimg
        self.newslink = newslink
    
    def getJSONFormatted(self):
        return {
            "quote": {
                "text": self.quote,
                "reddit_url": self.quoteurl
            },
            "image": {
                "image": self.imageurl,
                "title": self.imagetitle,
                "reddit_url": self.imageposturl
            },
            "news": {
                "url": self.newsurl,
                "title": self.newstitle,
                "description": self.newsdesc,
                "image": self.newsimg,
                "reddit_url": self.newslink
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
    
    randI, randQ, randN = (randint(0, len(imgpost) - 1),randint(0, len(quotepost) - 1),randint(0, len(newsPost) - 1))


    newsDesc, newsImage, newsTitle = None, None, None
    if len(newsPost) > 0:
        newsDesc, newsImage, newsTitle = NewsParser.parseArticle(newsPost[randN].content)


    if newsTitle == '' or not newsDesc == newsPost[randN].title:
        newsTitle = newsPost[randN].title

    quote = ''
    if len(quotepost[randQ].content) > len(quotepost[randQ].title):
        quote = quotepost[randQ].content
    else:
        quote = re.sub(r'\[text\]', '', quotepost[randQ].title, flags=re.IGNORECASE)

    return MediaSet(quote, quotepost[randQ].link,
                    imgpost[randI].image, imgpost[randI].title,  imgpost[randI].link,
                    newsPost[randN].content, newsTitle, newsDesc, newsImage, newsPost[randN].link)

