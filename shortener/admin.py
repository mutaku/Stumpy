from shortener.models import stumps
from django.contrib import admin

class stumpsAdmin(admin.ModelAdmin):
	list_display = ('longurl','shorturl','created','hits','cookie')
	search_fields = ['longurl','cookie']	
	date_hierarchy = 'created'

admin.site.register(stumps,stumpsAdmin)
