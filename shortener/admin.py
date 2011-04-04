from shortener.models import url
from django.contrib import admin

class urlAdmin(admin.ModelAdmin):
	list_display = ('longurl','shorturl','created','hits','cookie')
	search_fields = ['longurl','cookie']	
	date_hierarchy = 'created'

admin.site.register(url,urlAdmin)
