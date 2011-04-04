from django.http import HttpResponse
from django import forms
from shortener.models import stumps
from django.utils.encoding import smart_str
from django.shortcuts import get_object_or_404

def index(request):
	thetumps = stumps.objects.all()
	return HttpResponse(thestumps)


def detail(request,short):
	thisurl = get_object_or_404(stumps,shorturl=short)
	fullurl = thisurl.longurl	
	thisurl.hits += 1
	thisurl.save()
	return HttpResponse("You use short link %s which is translating to %s" % (short,fullurl))

def submit(request,stump):
	b = stumps(longurl=smart_str(stump))
	b.save()
	thisid = b.id	
	short = stumps.objects.get(id=thisid).shorturl
	long = stumps.objects.get(id=thisid).longurl 
	return HttpResponse("Added %s ==> %s" % (long,short))
