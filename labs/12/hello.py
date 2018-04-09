from flask import Flask
from random import randint
import datetime
import feedparser
app = Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"


@app.route("/")
def hello_world():
    return "Hello, world"


@app.route("/date")
def date():
    now = str(datetime.datetime.now())
    return now


@app.route("/hello/<name>")
def hello_name(name):
    return "Hello %s" % name


@app.route("/feed")
def feed():
    feed = feedparser.parse(BBC_FEED)
    randArt = randint(0, 9)
    article = feed['entries'][randArt]
    return """<html>
    <body>
    <h1> BBC headline </h1>
    <b>{0}</b> <br/>
    <i>{1}</i> <br/>
    <p>{2}</p> <br/>
    </body>
    </html>""".format(article.get("title"),
                      article.get("published"), article.get("summary"))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
