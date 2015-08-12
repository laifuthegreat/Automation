import tweepy
from CustomClasses import Pair
from Input import put_in_pair

def search_twitter(query):
	auth = tweepy.OAuthHandler('yqL0bnIQaED8MupuRGy4R2dPV', 'qqDmImPmzkj93ecRZY9IohibH1GrXavpWTlxbnCyfQ9qphPXU0')
	auth.set_access_token('526067745-Hg49IRfdy8T3XlJ5FYsx8yJBrDuO2L1Ixiv6f4Ep', 'IdoahCu3BK8935J5koE3ap2dn9EgP2B1d2n29EGzlwrIB')
	api = tweepy.API(auth)
	results = api.search_users(query)
	return_list = []
	for i in range(0, 7):
		if i < len(results):
			return_list.append(Pair(results[i].description, "https://twitter.com/{sn}".format(sn=results[i].screen_name)))
	return put_in_pair(return_list)