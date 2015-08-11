import csv
import URLtools
import feedparser
import urllib.request
import urllib.parse

in_reader = csv.reader(open("io/input/unchecked_links.csv", "r"), skipinitialspace=True)

def check_google(url):
	url = URLtools.base_url(url)
	url = URLtools.strip_url(url)
	if url == "google.com":
		return True
	else:
		return False

def check_url(name, url):
	url = URLtools.base_url(url).lower()
	if name == "Facebook":
		return "facebook.com" in url
	elif name == "Twitter":
		return "twitter.com" in url
	elif name == "YouTube":
		return "youtube.com" in url
	elif name == "LinkedIn":
		return "linkedin.com" in url
	elif name == "Google +":
		return "plus.google.com" in url
	elif name == "Instagram":
		return "instagram.com" in url
	elif name == "Flickr":
		return "flickr.com" in url
	else:
		return False

def test(network_name, site_url):
	try:
		req = urllib.request.Request(site_url,
									data=None,
									headers={
										'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
										}
									)
		f = urllib.request.urlopen(req)
	except (urllib.error.URLError, urllib.error.HTTPError, ConnectionResetError):
		print(line[1]+" "+line[2]+" 404")
	if not check_url(network_name, site_url):
		print(line[1]+" "+line[2])

outer = {}

def check_duplicates(university, network):
	if not university in outer:
		outer[university] = []
		outer[university].append(network)
	else:
		if network in outer[university]:
			print(university + " " + network)
		else:
			outer[university].append(network)

def fix_name(line_ls):
	new_name = ""
	ls = line_ls[1].split()
	for i in range(len(ls)):
		if ls[i] == "Univ":
			ls[i] = "University"
		new_name += ls[i]
		if i != len(ls)-1:
			new_name += " "
	return new_name


for line in in_reader:
	line[1] = fix_name(line)
	check_duplicates(line[1], line[2])
	if line[2] == "RSS":
		if not feedparser.parse(line[3])['items']:
			print(line[1]+" "+line[2])
		url = URLtools.garnish_url(line[3])
	else:
		url = URLtools.garnish_url(line[3])
		test(line[2], url)
	if check_google(url):
		print(line[1]+" "+line[2]+" weird google url")
