import csv
import FeedCreator
from Search import do_search
from Scan import Scan
import urllib
from Search import do_search1
import time

def Automate(input_file, official_file):
	inst_dict = Read_Official(official_file)
	myfile = open('new_file.csv', 'w', newline='')
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	f = open(input_file, 'r')
	for s in f:
		ls = s.split(',')
		name = fix_name(ls[1])
		print(name)
		try:
			print_list = create_print(name, inst_dict[name])
		except KeyError:
			print_list = create_print1(name)
		wr.writerow(print_list)

def are_same(url1, url2):
	return strip_prefix(url1).lower() == strip_prefix(url2).lower()

def strip_prefix(url):
	if url[:7]=="http://":
		url = url[7:]
	elif url[:8]=="https://":
		url = url[8:]
	if url[:4]=="www.":
		url = url[4:]
	return url

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
	for s in f:
		ls = s.split(',')
		if ls[1] != "":
			if ls[1][:7] != "http://":
				x = "http://"+ls[1]
			else:
				x = ls[1]
			inst_dict[ls[0]] = x
		else:
			continue
	return inst_dict

def create_print(name, site_url):
	time.sleep(2)
	ls = []
	ls.append(name)
	curr = Scan(site_url, "facebook")
	if curr:
		nx = do_search(name, "facebook")
		if not are_same(nx, curr):
			print("______________")
			print(curr)
			print(nx)
			curr = pick(curr, nx)
		ls.append(curr)
	else:
		ls.append(do_search(name, "facebook"))
	time.sleep(2)
	curr = Scan(site_url, "twitter")
	if curr:
		nx = do_search(name, "twitter")
		if not are_same(nx, curr):
			curr = pick(curr, nx)
		ls.append(curr)
	else:
		ls.append(do_search(name, "twitter"))
	time.sleep(2)
	curr = Scan(site_url, "youtube")
	if curr:
		nx = do_search(name, "youtube")
		if not are_same(nx, curr):
			curr = pick(curr, nx)
		ls.append(curr)
	else:
		ls.append(do_search(name, "youtube"))
	time.sleep(2)
	curr = Scan(site_url, "linkedin")
	if curr:
		nx = do_search(name, "linkedin")
		if not are_same(nx, curr):
			curr = pick(curr, nx)
		ls.append(curr)
	else:
		ls.append(do_search(name, "linkedin"))
	time.sleep(2)
	curr = Scan(site_url, "rss")
	if curr:
		ls.append(curr)
	else:
		try:
			curr = Scan(do_search1(name+" news"), "rss")
		except urllib.error.URLError:
			curr = None
		if not curr:
			curr = FeedCreator.create_feed(name)
		ls.append(curr)
	return ls

def pick(url1, url2):
	print("CONFLICT! Would you like to use (1): {u1} or (2): {u2}".format(u1=url1,u2=url2))
	x = input()
	if x == "1":
		return url1
	else:
		return url2

def create_print1(name):
	time.sleep(2)
	ls = []
	ls.append(name)
	ls.append(do_search(name, "facebook"))
	time.sleep(2)
	ls.append(do_search(name, "twitter"))
	time.sleep(2)
	ls.append(do_search(name, "youtube"))
	time.sleep(2)
	ls.append(do_search(name, "linkedin"))
	time.sleep(2)
	try:
		curr = Scan(do_search1(name + " news"), "rss")
	except urllib.error.URLError:
		curr = None
	time.sleep(2)
	if not curr:
		curr = FeedCreator.create_feed(name)
	ls.append(curr)
	return ls