from flask import Flask, render_template, request
import feedparser
app = Flask(__name__)

FEEDS = {
    "bbc": "http://feeds.bbci.co.uk/news/rss.xml",
    "aljazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "ap": "http://hosted2.ap.org/atom/APDEFAULT/cae69a7523db45408eeb2b3a98c0c9c5"
}


@app.route("/")
def feed():
    publication = ""
    if request.args.get("publication"):
        publication = request.args.get("publication")
    if not publication or publication.lower() not in FEEDS:
        publication = "bbc"
    feed = feedparser.parse(FEEDS[publication])
    articles = feed['entries']
    return render_template("feed.html", articles=articles, publication=publication)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
