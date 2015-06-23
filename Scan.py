import urllib.request
import re
from bs4 import BeautifulSoup

def Scan(url, network):
	x = find_network(network)
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html)
	if x != "rss":
		y = soup.find_all('a', href=re.compile(x))
	else:
		y = soup.find_all('a', href=re.compile("rss|feed|.xml"))
	if y[0]:
		return y[0]['href']
	return None

def find_network(network):
	x = network
	if x != "rss":
		x += ".com/"
	return x

print(Scan("http://www.appstate.edu/", "rss"))