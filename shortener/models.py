from django.db import models
import base62,hashlib


class url(models.Model):
	"database layout for storing the urls and statistics"
	longurl = models.URLField("Original URL",help_text="URL for shortening",max_length=2000,verify_exists=True)
	hashurl = models.CharField("Hash of original URL",max_length=70,null=True,blank=True,editable=False)
	# creating the short url
	def createShortURL(self):
		thisurl = self.longurl
		thisentry = url.objects.get(longurl=thisurl)
		theid = thisentry.id
		theshorty = base62.encode(theid)
		url.objects.filter(id=theid).update(shorturl=theshorty)
	shorturl = models.CharField("Shortened URL",max_length=15,null=True,blank=True,editable=False)
	hits = models.PositiveIntegerField("Number of visits",default=1,editable=False)
	created = models.DateTimeField("Created timestamp",auto_now=True,editable=False)
	lastvisit = models.DateTimeField("Last visit timestamp",auto_now_add=True,editable=False,)
	cookie = models.CharField("Associated cookie",max_length=10,null=True,blank=True,editable=False)
	def __unicode__(self):
		return u"%s ==> %s [created:%s | visits:%s | lastvisit:%s | associated cookie:%s ]" %(self.longurl,self.shorturl,self.created,self.hits,self.lastvisit,self.cookie) 
	# override the default save to create some callable functions
	def save(self, *args, **kwargs):
		# make a shorturl holder until we can get this id
		self.shorturl = "EMPTY"
		# create the hash url from the longurl
		self.hashurl = hashlib.sha1(self.longurl).hexdigest()
		if url.objects.filter(hashurl=self.hashurl):
			def __unicode__(self):
				return u"Url already available at %s" %(str(url.objects.get(hashurl=self.hashurl).shorturl))
		else:
			super(url, self).save(*args, **kwargs)
			# create the shorturl now that we can get an id (post insert) 
			self.createShortURL()
			def __unicode__(self):
				return u"%s ==> %s" %(self.longurl,self.shorturl)
