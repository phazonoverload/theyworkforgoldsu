from flask import Flask
from flask import render_template
import feedparser
app = Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"


@app.route("/hello/<name>")
def hello_name(name=None):
    return render_template("hello.html", name=name)


@app.route("/feed")
def feed():
    feed = feedparser.parse(BBC_FEED)
    articles = feed['entries']
    return render_template("feed.html", articles=articles)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
