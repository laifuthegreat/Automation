from urllib.parse import urlsplit, urlparse

import re

def are_same(url1, url2):
	return strip_url(url1)==strip_url(url2)

def base_url(url):
	return "{0.scheme}://{0.netloc}/".format(urlsplit(url))

def strip_url(url):
	if url != "":
		while url[-1] == "/":
			url = url[:-1]
	if url[:7] == "http://":
		url = url[7:]
	elif url[:8] == "https://":
		url = url[8:]
	if url[:4] == "www.":
		url = url[4:]
	return url

def garnish_url(url):
	url = strip_url(url)
	url = "http://" + url
	return url

def is_local(url):
	return urlparse(url).scheme == '' and url[:2] != '//'
	
def is_valid(url):
	return urlparse(url).scheme == ('http' or 'https') or url[:2] == '//'
