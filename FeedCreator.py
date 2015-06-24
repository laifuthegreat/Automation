def create_feed(name):
	ls = name.split()
	feed = "http://news.google.com/news?um=1&ned=us&hl=en&q="
	for x in ls:
		feed = feed + "+" + x
	feed = feed + "&output=rss"
	return feed