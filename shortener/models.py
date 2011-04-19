from django.db import models
from django.core.exceptions import ValidationError
import base62
import hashlib

class stumps(models.Model):
	longurl = models.URLField("Original URL",help_text="URL for shortening",max_length=2000,verify_exists=True)
	hashurl = models.CharField("Hash of original URL",max_length=70,editable=False,unique=True)
	shorturl = models.CharField("Shortened URL",max_length=15,null=True,blank=True,editable=False)
	hits = models.PositiveIntegerField("Number of visits",default=1,editable=False)
	lastvisit = models.DateTimeField("Last visit timestamp",auto_now_add=True,editable=False,)
	created = models.DateTimeField("Created timestamp",auto_now=True,editable=False)
	cookie = models.CharField("Associated cookie",max_length=10,null=True,blank=True,editable=False)

	def createShortURL(self):
		thisurl = self.longurl
		thisentry = stumps.objects.get(longurl=thisurl)
		theid = thisentry.id
		theshorty = base62.Encode(theid).string
		stumps.objects.filter(id=theid).update(shorturl=theshorty)

	def __unicode__(self):
		return u"%s ==> %s" %(self.longurl,self.shorturl) 

	def save(self, *args, **kwargs):
		super(stumps, self).save(*args, **kwargs)
		if not self.shorturl:
			self.createShortURL()

        def long_to_less_long(self):
                if len(self.longurl)>50:
                        return self.longurl[:50]+"..."
                else:
                        return self.longurl

