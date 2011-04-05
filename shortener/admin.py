from shortener.models import stumps
from django.contrib import admin

class stumpsAdmin(admin.ModelAdmin):
	list_display = ('long_to_less_long','shorturl','hashurl','created','hits','cookie')
	search_fields = ['longurl','cookie']	
	date_hierarchy = 'created'

admin.site.register(stumps,stumpsAdmin)
