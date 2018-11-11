import media
from flask import Flask, render_template, jsonify
import APIMedia as apMedia

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
    return jsonify(apMedia.agregate('aww', 'motivationalquotes','Uplifting news'))#TODO Subreddit Selector



if __name__ == '__main__':
    app.run(debug=True)