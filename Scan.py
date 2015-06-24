import urllib.request
import re
import feedparser
from bs4 import BeautifulSoup

def Scan(url, network):
	x = find_network(network)
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html)
	if x != "rss":
		y = soup.find_all('a', href=re.compile(x))
		if y:
			return y[0]['href']
	else:
		y = soup.find_all('a', type=re.compile("rss|xml|feed|atom"))
		for k in y:
			z = k['href']
			if not "http://www." in z:
				z = url[:-1] + z
			d = feedparser.parse(z)
			try:
				d['feed']['title']
				return z
			except KeyError:
				continue
	return None

def find_network(network):
	x = network
	if x != "rss":
		x += ".com/"
	return x