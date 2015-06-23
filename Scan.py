import urllib.request
import re
from bs4 import BeautifulSoup

def Scan(url, network):
	x = find_network(network)
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html)
	if x != "RSS":
		y = soup.find_all('a', href=re.compile(x))
	return y

def find_network(network):
	x = network
	if x != "RSS":
		x += ".com/"
	return x

print(Scan("http://www.bu.edu", "twitter")[0])