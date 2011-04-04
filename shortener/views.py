from django.http import HttpResponse,Http404
from django import forms
from shortener.models import stumps
from django.utils.encoding import smart_str
from django.shortcuts import get_object_or_404,get_list_or_404,render_to_response,redirect
import hashlib

def index(request):
	stumps_list = stumps.objects.all().order_by('-created')[:5]
	# like this way better but doesnt work this way
	#stumps_list = get_list_or_404(stumps).order_by('-created')[:5]
	return render_to_response('stumpy/index.html', {'stumps_list': stumps_list})	

def detail(request,short):
	thisurl = get_object_or_404(stumps,shorturl=short)
	fullurl = thisurl.longurl	
	thisurl.hits += 1
	thisurl.save()
	# this is non template driven for now becuase it will soon simply cause a redirect to real link (longurl)
	return HttpResponse("You use short link %s which is translating to %s" % (short,fullurl))
	# this is the redirect to be used
	#return redirect(fullurl)

def submit(request,stump):
	try:
		a = smart_str(stump)
		b = hashlib.sha1(a).hexdigest()
		c = stumps(longurl=a,hashurl=b)
		c.save()
		thisid = c.id	
		short = stumps.objects.get(id=thisid).shorturl
		long = stumps.objects.get(id=thisid).longurl 
		return HttpResponse("Added %s ==> %s" % (long,short))
	except:
		raise Http404
