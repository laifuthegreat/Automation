import urllib.parse

def create_feed(name):
	feed = "http://news.google.com/news?um=1&ned=us&hl=en&q="
	feed += urllib.parse.quote_plus(name)
	feed += "&output=rss"
	return feed