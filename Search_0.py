from py_bing_search import PyBingSearch
from Input import put_in

def search_network(term, network):
    print("Searching the web for {n1} {k} links".format(n1 = term, k = network))
    bing = PyBingSearch('yXlEmneFQ2MSqQfG3+8+5vrpLC6Kks+Fg8Z+4cP14cA')
    sitesearch = get_site_search(network)
    result_list, next_uri = bing.search("{t1} ({t2})".format t1 = sitesearch, t2 = term, limit=5, format='json')
    url_ls = []
    for result in result_list:
        url_ls.append(result.url)
    return put_in(url_ls)

def get_site_search(network):
    if network == "youtube":
        return "(site:youtube.com/user/ or site:youtube.com/channel/)"
    else:
        return "(site:{nt}.com)".format(nt=network)

def search(term):
    print("Searching the web for {n1} links".format(n1 = term))
    bing = PyBingSearch('yXlEmneFQ2MSqQfG3+8+5vrpLC6Kks+Fg8Z+4cP14cA')
    result_list, next_uri = bing.search(term, limit=5, format='json')
    url_ls = []
    for result in result_list:
        url_ls.append(result.url)
    return put_in(url_ls)