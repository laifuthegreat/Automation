from pws import Google
from Search import fix_term

term = input()
search_term = fix_term(term)
print(Google.search(search_term + " -site:google.com", 5, 0)['url'])