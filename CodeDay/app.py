import media
from flask import Flask, render_template, jsonify
import APIMedia as apMedia
from random import randint
from APIMedia import MediaSet

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

    agregatedData = apMedia.agregate(subredditsForImages[randint(0, len(subredditsForImages) - 1)],
                                    subredditsForNews[randint(0, len(subredditsForNews) - 1)],
                                    subredditsForQuotes[randint(0, len(subredditsForQuotes) - 1)])

    return jsonify(agregatedData.getJSONFormatted())#TODO Subreddit Selector




if __name__ == '__main__':
    app.run(debug=True)