from django.http import HttpResponse
from django import forms
from shortener.models import url

def index(request):
	stumps = url.objects.all()
	return HttpResponse(stumps)


def detail(request,short):
	fullurl = url.objects.get(shorturl=short).longurl
	return HttpResponse("You use short link %s which is translating to %s" % (short,fullurl))

def submit(request,url):
	return HttpResponse("Adding link %s" % url)
