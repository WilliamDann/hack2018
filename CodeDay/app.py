import media
from flask import Flask, render_template, jsonify
import APIMedia as apMedia
from random import randint
from APIMedia import MediaSet
import reddit

from ZODB import FileStorage, DB


from ZODB import FileStorage, DB

app = Flask(__name__, static_url_path='/static')
storage = FileStorage.FileStorage('ourDatabase.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/posts', methods=['GET'])
def getPosts():
    #TODO Jsonify the 
    """{
        "quote": "Very inspirational quote here",
        "image": {
        "title": "Cute cat",
        "url": "https://imgur.com/cat"
    },
        "news": {
        "title": "Something happy happened",
        "url": "https://news.com/happy"
    }
    }"""


    subredditsForImages = ['aww','funny','happy','cute','MadeMeSmile','GetMotivated','Aww']
    subredditsForQuotes = ['inspirationalquotes', 'happy', 'GetMotivated']
    subredditsForNews = ['UpliftingNews', 'upliftingtrends','happy']

    agregatedData = apMedia.agregate(subredditsForImages[randint(0, len(subredditsForImages) - 1)],
                                    subredditsForQuotes[randint(0, len(subredditsForQuotes) - 1)],
                                     subredditsForNews[randint(0, len(subredditsForNews) - 1)])

    return jsonify(agregatedData.getJSONFormatted())#TODO Subreddit Selector


def populateDB(listofimages, listofquotes, listofnews):
    joinedList = listofimages + listofquotes + listofnews
    for element in joinedList:
        #reddit = reddit.getPosts(element)
        root[element] = {mediaObj: reddit.getPosts(element)}







if __name__ == '__main__':
    app.run(debug=True)