from django.http import HttpResponse
from django import forms
from shortener.models import url
from django.utils.encoding import smart_str
from django.shortcuts import get_object_or_404

def index(request):
	stumps = url.objects.all()
	return HttpResponse(stumps)


def detail(request,short):
	thisurl = get_object_or_404(url,shorturl=short)
	fullurl = thisurl.longurl	
	thisurl.hits += 1
	thisurl.save()
	return HttpResponse("You use short link %s which is translating to %s" % (short,fullurl))

def submit(request,stump):
	b = url(longurl=smart_str(stump))
	b.save()
	thisid = b.id	
	short = url.objects.get(id=thisid).shorturl
	long = url.objects.get(id=thisid).longurl 
	return HttpResponse("Added %s ==> %s" % (long,short))
