# Automation
Project to automatically parse google results and university websites to find relevant social networks:

Usage:
	Put the input Member List CSV in io/input/
	Run Do.py
	write the member list filename
	write the database filename
	follow on-screen prompts
	Output is in io/output/o_file.csv
	Make sure you backup what's already in the output file before starting the program; the program will overwrite what's there

Prerequisites:
	Python 3.4+
	Python Modules (can be installed by running env-setup.bat):
		beautifulsoup4
		feedparser
		google-api-python-client
		tweepy
		py-bing-search