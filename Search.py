from py_bing_search import PyBingSearch
import time
from Input import put_in_pair
from Custom_Classes import Pair

def search_network(term, network):
    print("Searching the web for {n1} {k} links".format(n1 = term, k = network))
    time.sleep(0.5)
    bing = PyBingSearch('xj/imNsLFqGQ2RTMdiyduENDdqYy2PMLNCjztSlG3hs')
    sitesearch = get_site_search(network)
    result_list, next_uri = bing.search("{t1} ({t2})".format(t1 = sitesearch, t2 = term), limit=5, format='json')
    url_ls = []
    for result in result_list:
        url_ls.append(Pair(result.title, result.url))
    return put_in_bing(url_ls)

def get_site_search(network):
    if network == "youtube":
        return "(site:youtube.com/user/ OR site:youtube.com/channel/)"
    else:
        return "(site:{nt}.com)".format(nt=network)

def search(term):
    print("Searching the web for {n1} links".format(n1 = term))
    time.sleep(0.5)
    bing = PyBingSearch('xj/imNsLFqGQ2RTMdiyduENDdqYy2PMLNCjztSlG3hs')
    result_list, next_uri = bing.search(term, limit=5, format='json')
    url_ls = []
    for result in result_list:
        url_ls.append(Pair(result.title, result.url))
    return put_in_pair(url_ls)
