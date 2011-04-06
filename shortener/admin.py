from shortener.models import stumps
from django.contrib import admin
import hashlib

class stumpsAdmin(admin.ModelAdmin):
	list_display = ('long_to_less_long','shorturl','hashurl','created','hits','cookie')
	search_fields = ['longurl','cookie']	
	date_hierarchy = 'created'

	def save_model(self,request,obj,form,change):
		obj.hashurl = hashlib.sha1(obj.longurl).hexdigest()	
		obj.save()

admin.site.register(stumps,stumpsAdmin)








