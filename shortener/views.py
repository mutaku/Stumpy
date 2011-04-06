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
import bleach

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
	short_clean = bleach.clean(short)
	thisurl = get_object_or_404(stumps,shorturl=short_clean)
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
		stump_clean = bleach.clean(stump)
		this_stump = smart_str(stump_clean)
		this_user = smart_str(request.user)
		parsed_url = urlparse.urlparse(this_stump)
		stumpy_domain = smart_str(Site.objects.get_current().domain)
		if parsed_url.netloc != stumpy_domain:
			this_hash = hashlib.sha1(a).hexdigest()
			s = stumps(longurl=this_stump,hashurl=this_hash,cookie=this_user)
			s.save()
			this_id = s.id	
			new_stump = stumps.objects.get(id=this_id)
			stumpy_domain = smart_str(Site.objects.get_current().domain)
			return render_to_response('stumpy/submit.html', {
				'new_stump': new_stump,
				'stumpy_domain': stumpy_domain
			})
		else:
			return HttpResponse("Sly fox eats the poisoned rabbit.")
	except:
		raise Http404
