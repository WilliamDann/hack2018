import media
from flask import Flask, render_template, jsonify
import APIMedia as apMedia
from random import randint
from APIMedia import MediaSet
import reddit
import datetime

from ZODB import FileStorage, DB
import transaction


app = Flask(__name__, static_url_path='/static')
storage = FileStorage.FileStorage('data/ourDatabase.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

subredditsForImages = ['aww','funny','happy','cute','MadeMeSmile','GetMotivated','Awww']
subredditsForQuotes = ['inspirationalquotes', 'happy', 'GetMotivated']
subredditsForNews = ['UpliftingNews', 'upliftingtrends','happy']

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

    agregatedData = apMedia.agregate(subredditsForImages[randint(0, len(subredditsForImages) - 1)],
                                    subredditsForQuotes[randint(0, len(subredditsForQuotes) - 1)],
                                     subredditsForNews[randint(0, len(subredditsForNews) - 1)])

    return jsonify(agregatedData.getJSONFormatted())#TODO Subreddit Selector


def populateDB(listofimages, listofquotes, listofnews):
    connection = db.open()
    joinedList = listofimages + listofquotes + listofnews
    for element in joinedList:
        redditAsListMedObj = reddit.getPostsAsMediaObjects(element)
        root[element] = {"mediaObj": redditAsListMedObj, "timeUpdate": str(datetime.datetime.now())}
    transaction.commit()
    connection.close()

populateDB(subredditsForImages, subredditsForQuotes, subredditsForNews)
print(root.items())


if __name__ == '__main__':
    app.run(debug=True)
