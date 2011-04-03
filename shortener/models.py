from django.db import models


class urls(models.Model):
	"database layout for storing the urls and statistics"
	longurl = models.URLField("Original URL",max_length=2000,verify_exists=True)
	hashurl = models.CharField("Hash of original URL",max_length=60)
	shorturl = models.CharField("Shortened URL",max_length=15,null=True)
	hits = models.PositiveIntegerField("Number of visits",default=1)
	created = models.DateTimeField("Created timestamp",auto_now=True)
	lastvisit = models.DateTimeField("Last visit timestamp",auto_now_add=True)
	cookie = models.CharField("Associated cookie",max_length=10,null=True)
