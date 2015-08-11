import csv
import FeedCreator
from Search import *
from Scan import Scan
import urllib
import urllib.request
import time
from URLtools import *
import urllib.parse
import socket

def Automate(input_file):
	myfile = open('io/output/o_file.csv', 'w', newline='')
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	f = open('io/input/'+input_file, 'r')
	m_reader = csv.reader(f, skipinitialspace = True)
	for ls in m_reader:
		name = fix_name(ls[1])
		print("_________________________________")
		print("{n1} ({l1}, {l2}):".format(n1=name, l1=ls[2], l2=ls[3]))
		if ls[4] != "":
			webmail = ['yahoo.com', 'gmail.com', 'outlook.com', 'live.come', 'hotmail.com', 'aol.com', 'icloud.com']
			x = ls[4]
			if not x in webmail:
				x = "http://{url}".format(url=x)
			else:
				x = None
		if not x:
			print_list = create_print1(name)
		else:
			print_list = create_print(name, x)
		wr.writerow(print_list)

def fix_name(input_string):
	if "Univ" in input_string:
		ls = input_string.split()
		i = 0
		rS = ""
		while i < len(ls):
			if i != 0:
				rS += " "
			if ls[i] != "Univ":
				rS += ls[i]
			else:
				rS += "University"
			i += 1
	else:
		rS = input_string
	return rS

def find_link(name, site_url, html, network, out_ls):
	if html:
		curr = Scan(site_url, html, network)
		if curr:
			out_ls.append(curr)
			return
	out_ls.append(search_network(name, network))


def create_print(name, site_url):
	ls = []
	ls.append(name)
	try:
		html = get_html(site_url)
	except (AttributeError, ConnectionResetError, ValueError, socket.timeout, urllib.error.HTTPError, urllib.error.URLError):
		html = False
	find_link(name, site_url, html, "facebook", ls)
	find_link(name, site_url, html, "twitter", ls)
	find_link(name, site_url, html, "youtube", ls)
	find_link(name, site_url, html, "linkedin", ls)
	curr = None
	if html:
		curr = Scan(site_url, html, "rss")
	if not curr:
		curr = find_rss(name)
	ls.append(curr)
	return ls

def get_html(url):
	req = urllib.request.Request(url,
								data=None,
								headers={
									'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
									}
								)
	html = urllib.request.urlopen(req, timeout = 10).read()
	return html

def find_rss(name):
	rsslink = search(name + " news")
	curr = None
	if rsslink:
		try:
			curr = Scan(rsslink, get_html(rsslink), "rss")
		except (AttributeError, ConnectionResetError, ValueError, socket.timeout, urllib.error.HTTPError, urllib.error.URLError):
			curr = None
	if not curr:
		rsslink = search(name + " rss feeds")
		if rsslink:
			try:
				curr = Scan(rsslink, get_html(rsslink), "rss")
			except (AttributeError, ConnectionResetError, ValueError, socket.timeout, urllib.error.HTTPError, urllib.error.URLError):
				curr = None
		if not curr:
			rsslink = search(name + " blog")
			if rsslink:
				try:
					curr = Scan(rsslink, get_html(rsslink), "rss")
				except (AttributeError, ConnectionResetError, ValueError, socket.timeout, urllib.error.HTTPError, urllib.error.URLError):
					curr = None
			if not curr:
				rsslink = search(name + " calendar")
				if rsslink:
					try:
						curr = Scan(rsslink, get_html(rsslink), "rss")
					except (AttributeError, ConnectionResetError, ValueError, socket.timeout, urllib.error.HTTPError, urllib.error.URLError):
						curr = None
				if not curr:
					rsslink = search(name + " topix")
					if rsslink:
						try:
							curr = Scan(rsslink, get_html(rsslink), "rss")
						except (AttributeError, ConnectionResetError, ValueError, socket.timeout, urllib.error.HTTPError, urllib.error.URLError):
							curr = None
	if not curr:
		curr = FeedCreator.create_feed(name)
	return curr

def create_print1(name):
	ls = []
	ls.append(name)
	ls.append(search_network(name, "facebook"))
	ls.append(search_network(name, "twitter"))
	ls.append(search_network(name, "youtube"))
	ls.append(search_network(name, "linkedin"))
	curr = find_rss(name)
	ls.append(curr)
	return ls
