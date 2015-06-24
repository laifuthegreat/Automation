import csv
import FeedCreator
from Search import showsome
from Scan import Scan

def Automate(input_file, official_file):
	inst_dict = Read_Official(official_file)
	myfile = open('new_file.csv', 'wb')
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	f = open(input_file, 'r')
	for s in f:
		ls = s.split(',')
		name = fix_name(ls[1])
		try:
			print_list = create_print(name, inst_dict[name])
		except KeyError:
			print_list = create_print(name)
		wr.writerow(print_list)


def fix_name(input_string):
	if "Univ" in input_string:
		ls = input_string.split()
		i = 0
		rS = ""
		while i < len(ls):
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
			inst_dict[ls[0]] = ls[1]
		else:
			continue
	return inst_dict

def create_print(name, site_url):
	ls = []
	ls.append(name)
	curr = Scan(site_url, "facebook")
	if curr:
		next = showsome("{n} facebook site:facebook.com".format(n=name))
		if next != curr:
			curr = pick(curr, next)
		ls.append(curr)
	else:
		ls.append(showsome("{n} facebook site:facebook.com".format(n=name)))
	curr = Scan(site_url, "twitter")
	if curr:
		next = showsome("{n} twitter site:twitter.com".format(n=name))
		if next != curr:
			curr = pick(curr, next)
		ls.append(curr)
	else:
		ls.append(showsome("{n} twitter site:twitter.com".format(n=name)))
	curr = Scan(site_url, "youtube")
	if curr:
		next = showsome("{n} youtube site:youtube.com".format(n=name))
		if next != curr:
			curr = pick(curr, next)
		ls.append(curr)
	else:
		ls.append(showsome("{n} youtube site:youtube.com".format(n=name)))
	curr = Scan(site_url, "linkedin")
	if curr:
		next = showsome("{n} linkedin site:linkedin.com".format(n=name))
		if next != curr:
			curr = pick(curr, next)
		ls.append(curr)
	else:
		ls.append(showsome("{n} linkedin site:linkedin.com".format(n=name)))
	curr = Scan(site_url, "rss")
	if curr:
		ls.append(curr)
	else:
		curr = Scan(showsome("{n} news".format(n=name)), "rss")
		if not curr:
			curr = FeedCreator.create_feed(name)
		ls.append(curr)
	return ls

def pick(url1, url2):
	print("CONFLICT! Would you like to use (1): {u1} or (2): {u1}".format(u1=url1,u2=url2))
	x = input()
	if x == "1":
		return url1
	else:
		return url2

def create_print(name):
	ls = []
	ls.append(name)
	ls.append(showsome("{n} facebook site:facebook.com".format(n=name)))
	ls.append(showsome("{n} twitter site:twitter.com".format(n=name)))
	ls.append(showsome("{n} youtube site:youtube.com".format(n=name)))
	ls.append(showsome("{n} linkedin site:linkedin.com".format(n=name)))
	curr = Scan(showsome("{n} news".format(n=name)), "rss")
	if not curr:
		curr = FeedCreator.create_feed(name)
	ls.append(curr)
	return ls