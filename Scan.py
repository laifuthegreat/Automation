import urllib.request
from urllib.parse import urlsplit
import re
import feedparser
from bs4 import BeautifulSoup
import winsound

def Scan(url, network):
	print("Scanning {u} for {k} links".format(u = url, k = network))
	x = find_network(network)
	try:
		html = urllib.request.urlopen(url).read()
	except AttributeError:
		return None
	soup = BeautifulSoup(html)
	if x != "rss":
		y = soup.find_all('a', href=re.compile(x))
		if y:
			if len(y) > 1:
				i = 1
				for x in y:
					print(str(i)+" "+x['href'])
					i += 1
				print(str(i)+" None")
				winsound.Beep(1000,500)
				j = int(input())
				if not j <= len(y):
					return None
				return y[j-1]['href']
			else:
				return y[0]['href']
	else:
		y = soup.find_all('a', type=re.compile(".rss|.xml|feed|atom", re.IGNORECASE))
		if len(y) > 1:
			i = 1
			for k in y:
				z = k['href']
				if (not "http://" in z and not "https://" in z):
					
					base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
					z = base_url + z
					k['href'] = z
				print(str(i)+" "+z)
				i += 1
			print(str(i)+" None")
			winsound.Beep(1000,500)
			j = int(input())
			if not j == len(y) + 1:
				return y[j-1]['href']
		elif len(y) == 1:
			z = y[0]['href']
			if (not "http://" in z and not "https://" in z):
				
				base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
				z = base_url + z
			return z
		else:
			y = soup.find_all('a', href=re.compile("rss|xml|feed|atom", re.IGNORECASE))
			if len(y) > 1:
				i = 1
				for k in y:
					z = k['href']
					if (not "http://" in z and not "https://" in z):
						base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
						z = base_url + z
						k['href'] = z
					print(str(i)+" "+z)
					i += 1
				print(str(i)+" None")
				winsound.Beep(1000,500)
				j = int(input())
				if j == len(y)+1:
					return None
				return y[j-1]['href']
			elif len(y) == 1:
				z = y[0]['href']
				if (not "http://" in z and not "https://" in z):
					
					base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
					z = base_url + z
				return z
			# d = feedparser.parse(z)
			# try:
			# 	d['feed']['title']
			# 	return z
			# except KeyError:
			# 	continue
	return None

def find_network(network):
	x = network
	if x != "rss":
		x += ".com/"
	return x