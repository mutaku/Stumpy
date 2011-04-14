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
	stump_stats_num = stumps.objects.all().count()
	stump_stats_visits = stumps.objects.aggregate(Sum('hits'))['%s__sum' % 'hits']
	recent_stumps_list = stumps.objects.all().order_by('-id')[:5]
	famous_stumps_list = stumps.objects.all().order_by('-hits')[:5]
	return render_to_response('stumpy/index.html', {
		'stumpy_domain': stumpy_domain,
		'recent_stumps_list': recent_stumps_list, 
		'famous_stumps_list': famous_stumps_list,
		'stump_stats_num': stump_stats_num,
		'stump_stats_visits': stump_stats_visits
	})	

def detail(request,short):
	short_clean = bleach.clean(short)
	stump = get_object_or_404(stumps,shorturl=short_clean)
	stump.hits += 1
	stump.save()
	# this is non template driven for now becuase it will soon simply cause a redirect to real link (longurl)
	return HttpResponse("You used short link %s which is translating to %s" % (stump.shorturl,stump.longurl))
	# this is the redirect to be used
	#return redirect(stump.longurl)

@login_required
def submit(request,stump):
	stumpy_domain = smart_str(Site.objects.get_current().domain)
	stump_clean = bleach.clean(stump)
	this_stump = smart_str(stump_clean)
	this_hash = hashlib.sha1(this_stump).hexdigest()
	does_exist = stumps.objects.filter(hashurl=this_hash)
	if not does_exist:
		this_user = smart_str(request.user)
		parsed_url = urlparse.urlparse(this_stump)
		if parsed_url.netloc != stumpy_domain:
			s = stumps(longurl=this_stump,hashurl=this_hash,cookie=this_user)
			s.save()
			new_stump = stumps.objects.get(id=s.id)	
			stumpy_domain = smart_str(Site.objects.get_current().domain)
			return render_to_response('stumpy/submit.html', {
				'new_stump': new_stump,
				'stumpy_domain': stumpy_domain
			})
		else:
			return HttpResponse("Sly fox eats the poisoned rabbit.")
	else:
		return render_to_response('stumpy/submit.html', {
				'exist_stump': does_exist.get(),
				'stumpy_domain': stumpy_domain
			})
