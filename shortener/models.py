from django.db import models
from django.core.exceptions import ValidationError
import base62,hashlib


class stumps(models.Model):
	"database layout for storing the urls"
	longurl = models.URLField("Original URL",help_text="URL for shortening",max_length=2000,verify_exists=True)
	hashurl = models.CharField("Hash of original URL",max_length=70,editable=False,unique=True)
	# creating the short url
	def createShortURL(self):
		thisurl = self.longurl
		thisentry = url.objects.get(longurl=thisurl)
		theid = thisentry.id
		theshorty = base62.encode(theid)
		stumps.objects.filter(id=theid).update(shorturl=theshorty)
	shorturl = models.CharField("Shortened URL",max_length=15,null=True,blank=True,editable=False,unique=True)
	hits = models.PositiveIntegerField("Number of visits",default=1,editable=False)
	lastvisit = models.DateTimeField("Last visit timestamp",auto_now_add=True,editable=False,)
	created = models.DateTimeField("Created timestamp",auto_now=True,editable=False)
	cookie = models.CharField("Associated cookie",max_length=10,null=True,blank=True,editable=False)
	def __unicode__(self):
		return u"%s ==> %s [created:%s | visits:%s | lastvisit:%s | associated cookie:%s ]" %(self.longurl,self.shorturl,self.created,self.hits,self.lastvisit,self.cookie) 
	# override the default save to create some callable functions
	def save(self, *args, **kwargs):
		super(stumps, self).save(*args, **kwargs)
		# create the shorturl now that we can get an id (post insert) 
		if not self.shorturl:
			self.createShortURL()
