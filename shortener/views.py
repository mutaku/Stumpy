from django.http import HttpResponse,Http404
from django import forms
from shortener.models import stumps
from django.utils.encoding import smart_str
from django.shortcuts import get_object_or_404,get_list_or_404,render_to_response,redirect
import hashlib
import urlparse
from django.db.models import Sum,Count
from django.contrib.sites.models import Site
from django.contrib.auth.decorators import login_required

def index(request):
	stumpy_domain = smart_str(Site.objects.get_current().domain)
	stump_stats_num = stumps.objects.aggregate(Count('id'))['%s__count' % 'id']
	stump_stats_visits = stumps.objects.aggregate(Sum('hits'))['%s__sum' % 'hits']
	recent_stumps_list = stumps.objects.all().order_by('-id')[:5]
	famous_stumps_list = stumps.objects.all().order_by('-hits')[:5]
	# like this way better but doesnt work this way
	#stumps_list = get_list_or_404(stumps).order_by('-created')[:5]
	return render_to_response('stumpy/index.html', {
		'stumpy_domain': stumpy_domain,
		'recent_stumps_list': recent_stumps_list, 
		'famous_stumps_list': famous_stumps_list,
		'stump_stats_num': stump_stats_num,
		'stump_stats_visits': stump_stats_visits
	})	

# for now we just use this for testing - we don't want to inhibit url redirects for users because that defeats purpose
@login_required
def detail(request,short):
	thisurl = get_object_or_404(stumps,shorturl=short)
	fullurl = thisurl.longurl	
	thisurl.hits += 1
	thisurl.save()
	# this is non template driven for now becuase it will soon simply cause a redirect to real link (longurl)
	return HttpResponse("You use short link %s which is translating to %s" % (short,fullurl))
	# this is the redirect to be used
	#return redirect(fullurl)

# want login_required here to limit the submissions and so we can tag submissions to user names
@login_required
def submit(request,stump):
	try:
		a = smart_str(stump)
		thisuser = smart_str(request.user)
		parsedurl = urlparse.urlparse(a)
		stumpydomain = smart_str(Site.objects.get_current().domain)
		if parsedurl.netloc != stumpydomain:
			b = hashlib.sha1(a).hexdigest()
			c = stumps(longurl=a,hashurl=b,cookie=thisuser)
			c.save()
			thisid = c.id	
			newstump = stumps.objects.get(id=thisid)
			stumpy_domain = smart_str(Site.objects.get_current().domain)
			return render_to_response('stumpy/submit.html', {
				'newstump': newstump,
				'stumpy_domain': stumpy_domain
			})
		else:
			return HttpResponse("Sly fox eats the poisoned rabbit.")
	except:
		raise Http404
