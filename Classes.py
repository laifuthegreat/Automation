import urllib2

class Institution:

	def __init__(self, Name, Code, FaceBook, LinkedIn, Twitter, YouTube, RSS):
		self.name = Name
		self.code = Code
		self.facebook = FaceBook
		self.linkedin = LinkedIn
		self.twitter = Twitter
		self.youtube = YouTube
		self.rss = RSS

	def getSQL():
		SQLselect = "select"
		SQLselect = SQLselect + " " + self.code + ", "
		SQLselect = SQLselect + self.name + ", "
		SQLselect = SQLselect + self.facebook + ", "
		SQLselect = SQLselect + self.twitter + ", "
		SQLselect = SQLselect + self.linkedin + ", "
		SQLselect = SQLselect + self.youtube + ", "
		SQLselect = SQLselect + self.rss + "union"
		return SQLselect

	def getSQLBegin():
		SQLselect = "select"
		SQLselect = SQLselect + " " + self.code + "as Code, "
		SQLselect = SQLselect + self.name + "as Name, "
		SQLselect = SQLselect + self.facebook + "as Facebook, "
		SQLselect = SQLselect + self.twitter + "as Twitter, "
		SQLselect = SQLselect + self.linkedin + "as LinkedIn, "
		SQLselect = SQLselect + self.youtube + "as YouTube, "
		SQLselect = SQLselect + self.rss + "as RSS union"
		return SQLselect

	def getSQLEnd():
		SQLselect = "select"
		SQLselect = SQLselect + " " + self.code + ", "
		SQLselect = SQLselect + self.name + ", "
		SQLselect = SQLselect + self.facebook + ", "
		SQLselect = SQLselect + self.twitter + ", "
		SQLselect = SQLselect + self.linkedin + ", "
		SQLselect = SQLselect + self.youtube + ", "
		SQLselect = SQLselect + self.rss + ";"
		return SQLselect