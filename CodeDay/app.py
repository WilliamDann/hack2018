import media
from flask import Flask, render_template, jsonify
import APIMedia as apMedia
import random

app = Flask(__name__, static_url_path='/static')

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

    return jsonify(apMedia.agregate(subredditsForImages[random.int(0, len(subredditsForImages) - 1)],
                                    subredditsForNews[random.int(0, len(subredditsForNews) - 1)],
                                    subredditsForQuotes[random.int(0, len(subredditsForQuotes) - 1)]))#TODO Subreddit Selector



if __name__ == '__main__':
    app.run(debug=True)