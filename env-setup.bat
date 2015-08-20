echo installing python packages...
echo installing page scraper
py -m pip install --upgrade beautifulsoup4
echo installing RSS feed parser
py -m pip install --upgrade feedparser
echo installing youtube search api
py -m pip install --upgrade google-api-python-client
echo installing twitter search api
py -m pip install --upgrade tweepy
echo installing bing search api
py -m pip install --upgrade py-bing-search