import csv
import FeedCreator
from Search import *
from Scan import Scan
import urllib
import urllib.request
import time
from URLtools import *

def Automate(input_file, official_file):
	inst_dict = Read_Official('io/input/'+official_file)
	myfile = open('io/output/o_file.csv', 'w', newline='')
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	f = open('io/input/'+input_file, 'r')
	m_reader = csv.reader(f, skipinitialspace = True)
	for ls in m_reader:
		name = fix_name(ls[1])
		print("_________________________________")
		print(name + ":")
		try:
			print_list = create_print(name, inst_dict[name])
		except KeyError:
			x = search(name)
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

def Read_Official(input_file):
	inst_dict = {}
	f = open(input_file, 'r')
	r = csv.reader(f, skipinitialspace = True)
	for ls in r:
		if ls[1] != "":
			url = ls[1].lower()
			if not is_valid(url):
				x = garnish_url(url)
			else:
				x = url
			inst_dict[ls[0]] = x
		else:
			continue
	return inst_dict

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
		html = urllib.request.urlopen(site_url).read()
	except (AttributeError, ConnectionResetError, ValueError):
		html = False
	find_link(name, site_url, html, "facebook", ls)
	find_link(name, site_url, html, "twitter", ls)
	find_link(name, site_url, html, "youtube", ls)
	find_link(name, site_url, html, "linkedin", ls)
	if html:
		curr = Scan(site_url, html, "rss")
		if curr:
			ls.append(curr)
			return ls
	rsslink = search(name + " news")
	if rsslink:
		try:
			curr = Scan(rsslink, urllib.request.urlopen(rsslink), "rss")
		except (AttributeError, ConnectionResetError, ValueError):
			curr = None
	if not curr:
		curr = FeedCreator.create_feed(name)
	ls.append(curr)
	return ls

def create_print1(name):
	ls = []
	ls.append(name)
	ls.append(search_network(name, "facebook"))
	ls.append(search_network(name, "twitter"))
	ls.append(search_network(name, "youtube"))
	ls.append(search_network(name, "linkedin"))
	rsslink = search(name + " news")
	if rsslink:
		try:
			curr = Scan(rsslink, urllib.request.urlopen(rsslink), "rss")
		except (AttributeError, ConnectionResetError, ValueError):
			curr = None
	else:
		curr = None
	if not curr:
		curr = FeedCreator.create_feed(name)
	ls.append(curr)
	return ls