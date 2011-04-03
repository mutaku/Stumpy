from django.db import models

"""
old database setup
+----------+-------------+------+-----+-------------------+----------------+
| Field    | Type        | Null | Key | Default           | Extra          |
+----------+-------------+------+-----+-------------------+----------------+
| id       | int(15)     | NO   | PRI | NULL              | auto_increment | 
| longurl  | blob        | YES  |     | NULL              |                | 
| hash_url | varchar(60) | YES  |     | NULL              |                | 
| shorturl | varchar(15) | YES  |     | NULL              |                | 
| hits     | bigint(20)  | YES  |     | NULL              |                | 
| date     | timestamp   | NO   |     | CURRENT_TIMESTAMP |                | 
+----------+-------------+------+-----+-------------------+----------------+
"""

class urls(models.Model):
	"database layout for storing the urls and statistics"
	longurl = models.URLField("Original URL",max_length=2000,verify_exists=True)
	hashurl = models.CharField("Hash of original URL",max_length=60)
	shorturl = models.CharField("Shortened URL",max_length=15)
	hits = models.PositiveIntegerField("Number of visits")
	created = models.DateTimeField("Created timestamp",auto_now=True)
	lastvisit = models.DateTimeField("Last visit timestamp",auto_now_add=True)
	cookie = models.CharField("Associated cookie",max_length=10)
