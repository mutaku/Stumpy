from shortener.models import stump
from django.contrib import admin
import hashlib
from django.utils.encoding import smart_str

class stumpAdmin(admin.ModelAdmin):
	list_display = ('long_to_less_long','shorturl','hashurl','created','hits','cookie')
	search_fields = ['longurl','cookie']
	list_filter = ['created','lastvisit','cookie']	
	date_hierarchy = 'created'

	def save_model(self,request,obj,form,change):
		obj.hashurl = hashlib.sha1(obj.longurl).hexdigest()	
		obj.cookie = smart_str(request.user)
		obj.save()

admin.site.register(stump,stumpAdmin)








