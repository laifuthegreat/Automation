from pws import Google

def do_search(search_term, network):
	try:
		search_term = fix_term(search_term)
		return Google.search('{s1} site:{s2}.com -site:google.com'.format(s1=search_term, s2=network), 1, 0)['results'][0]['link'].split("&")[0]
	except AttributeError:
		return "None"

def do_search1(search_term):
	search_term = fix_term("{s1} -site:google.com".format(s1=search_term))
	x = Google.search(search_term, 1, 0)['results'][0]['link'].split("&")[0]
	return x

def fix_term(search_term):
	ls = search_term.split("&")
	search_term = ls[0]
	i = 1
	while i < len(ls):
		search_term += "%26"
		search_term += ls[i]
		i += 1
	return search_term