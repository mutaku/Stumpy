##########################################################
# chainsaw -
# Some Cookie Methods 
# not for security - merely for associating with a browser
##########################################################

class CreateCookie():
	"Generate a Cookie using given name"
	def __init__(self,NAME,HASH=""):
		from Cookie import SimpleCookie
		self.C = SimpleCookie()
		self.NAME = NAME
		self.HASH = HASH
		self.makeCookie()
	def makeHash(self):
		import hashlib,random
		self.R = str(random.random())
		self.H = hashlib
		self.FULLTOKEN = self.H.sha256(self.R).hexdigest()
		self.TOKEN = self.FULLTOKEN[:10]
		return self.TOKEN
	def makeCookie(self):
		if self.HASH:
			self.C[self.NAME] = self.HASH
		else:
			self.C[self.NAME] = self.makeHash() 
		print self.C

class GetCookie():
	"Retrieve cookie value or generate one if can't find it by given name"
	def __init__(self,NAME):
		from Cookie import SimpleCookie
		import os
		self.NAME = NAME
		if "HTTP_COOKIE" not in os.environ.keys():	
			CreateCookie(self.NAME)
		else:
			self.E = os.environ["HTTP_COOKIE"]
			self.C = SimpleCookie(self.E)	
			self.getToken()
	def getToken(self):
		try:
			self.TOKEN = self.C[self.NAME].value
			return self.TOKEN
		except:
			print "Can't find Cookie. Generating one."
			CreateCookie(self.NAME)

class CopyCookie():
	"Make a duplicate cookie from existing hash to tack in another browser"
	def __init__(self,NAME,HASH):
		self.HASH = HASH
		self.NAME = NAME
		if not self.HASH.isalnum() or len(self.HASH)>10:
			print "Improper hash."
		else:
			CreateCookie(self.NAME,self.HASH)
