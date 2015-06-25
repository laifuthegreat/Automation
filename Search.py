from pws import Google
import winsound

def do_search(search_term, network):
	print("Searching the web for {u} {k} links".format(u = search_term, k = network))
	try:
		search_term = fix_term(search_term)
		if network == "youtube":
			network += ".com/user/ OR site:youtube.com/channel/"
		else:
			network += ".com/"
		i =1
		g = Google.search('{s1} site:{s2} -site:google.com'.format(s1=search_term, s2=network), 5, 0)['results']
		for x in g:
			y = x['link'].split("&")[0]
			print(str(i)+" "+y)
			i+=1
		print(str(i)+" None")
		print(str(i+1)+" Manul Entry")
		winsound.Beep(1000,500)
		j = int(input())
		if j == len(g) + 1:
			return None
		elif j > len(g) + 1:
			print(">>>")
			winsound.Beep(1000,500)
			return input()
		return g[j-1]['link'].split("&")[0]
	except AttributeError:
		return "None"

def do_search1(search_term):
	try:
		print("Searching the web for {u}".format(u = search_term))
		search_term = fix_term("{s1} -site:google.com".format(s1=search_term))
		i = 1
		g = Google.search(search_term, 5, 0)['results']
		for x in g:
			y = x['link'].split("&")[0]
			print(str(i)+" "+y)
			i+=1
		print(str(i)+" None")
		print(str(i+1)+" Manul Entry")	
		winsound.Beep(1000,500)
		j = int(input())
		if j == len(g) + 1:
			return None
		elif j > len(g) + 1:
			print(">>>")
			winsound.Beep(1000,500)
			return input()
		return g[j-1]['link'].split("&")[0]
	except AttributeError:
		print("Error searching for {n}, hit enter to continue".format(n=search_term))
		winsound.Beep(1000,500)
		input()
		return None

def fix_term(search_term):
	ls = search_term.split("&")
	search_term = ls[0]
	i = 1
	while i < len(ls):
		search_term += "%26"
		search_term += ls[i]
		i += 1
	return search_term