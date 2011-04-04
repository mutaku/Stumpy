from django.http import HttpResponse
from django import forms
from shortener.models import stumps
from django.utils.encoding import smart_str
from django.shortcuts import get_object_or_404,render_to_response
import hashlib

def index(request):
	stumps_list = stumps.objects.all().order_by('-created')[:5]
	return render_to_response('stumpy/index.html', {'stumps_list': stumps_list})	

def detail(request,short):
	thisurl = get_object_or_404(stumps,shorturl=short)
	fullurl = thisurl.longurl	
	thisurl.hits += 1
	thisurl.save()
	# this is non template driven for now becuase it will soon simply cause a redirect to real link (longurl)
	return HttpResponse("You use short link %s which is translating to %s" % (short,fullurl))

def submit(request,stump):
	a = smart_str(stump)
	b = hashlib.sha1(a).hexdigest()
	c = stumps(longurl=a,hashurl=b)
	c.save()
	thisid = c.id	
	short = stumps.objects.get(id=thisid).shorturl
	long = stumps.objects.get(id=thisid).longurl 
	return HttpResponse("Added %s ==> %s" % (long,short))
