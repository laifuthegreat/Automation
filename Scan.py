from URLtools import *
from Input import put_in
import re
import feedparser
from bs4 import BeautifulSoup

def Scan(url, html, network):
	
	def build_url_list(soup_results):
		ls = []
		for result in soup_results:
			if is_local(result['href']):
				curr_url = base_url(url)+result['href'][1:]
			else:
				curr_url = result['href']
			curr_feed = feedparser.parse(curr_url)
			if curr_feed['items']:
				ls.append(curr_url)
		curr_page_feed = feedparser.parse(url)
		if curr_page_feed['items']:
			ls.append(url)
		return ls

	print("Scanning {u} for {k} links".format(u = url, k = network))
	x = find_network(network)
	soup = BeautifulSoup(html)
	if x != "rss":
		y = soup.find_all('a', href=re.compile(x))
		return put_in(build_url_list(y))
	else:
		y = soup.find_all('a', type=re.compile("rss+xml|atom", re.IGNORECASE))
		if not y:
			y = soup.find_all('a', href=re.compile("rss|\.xml$|(?!feedback|mailto:)feed|atom|subscribe", re.IGNORECASE))
		return put_in(build_url_list(y))

def find_network(network):
	x = network
	if x != "rss":
		x += ".com/"
	return x