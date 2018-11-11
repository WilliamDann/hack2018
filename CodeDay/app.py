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


subredditsForImages = ['aww','happy','cute','MadeMeSmile','GetMotivated','Awww', 'cats', 'toofers', 'blep', 'blop', 'puppers', 'corgibutts']
subredditsForQuotes = ['GetMotivated']
subredditsForNews = ['UpliftingNews', 'upliftingtrends']

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/posts', methods=['GET'])
def getPosts():

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

def updateDB(subredditName):
    newListOfMedObj = reddit.getPostsAsMediaObjects(subredditName)
    root[subredditName] = {"mediaObj": newListOfMedObj, "timeUpdate": str(datetime.datetime.now())}


if __name__ == '__main__':
    db = DB("data/ourDatabase.fs")
    connection = db.open()
    root = connection.root()

    # populateDB(subredditsForImages, subredditsForQuotes, subredditsForNews)
    print(root.items())

    app.run() # DO NOT ENABLE DEBUG
