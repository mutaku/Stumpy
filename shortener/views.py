from django.http import HttpResponse,Http404
from django import forms
from shortener.models import stump
from django.utils.encoding import smart_str
from django.shortcuts import get_object_or_404,get_list_or_404,render_to_response,redirect
import hashlib
import urlparse
import xml.sax.saxutils as X
from django.db.models import Sum,Count
from django.contrib.sites.models import Site
from django.contrib.auth.decorators import login_required
import bleach


def index(request):
	my_stumps = ""
	if request.user.is_authenticated():
		my_stumps = stump.objects.filter(cookie__iexact=request.user).order_by('-id')
	stumpy_domain = smart_str(Site.objects.get_current().domain)
	stump_stats_num = stump.objects.all().count()
	stump_stats_visits = stump.objects.aggregate(Sum('hits'))['%s__sum' % 'hits']
	recent_stumps_list = stump.objects.all().order_by('-id')[:5]
	famous_stumps_list = stump.objects.all().order_by('-hits')[:5]
	return render_to_response('stumpy/index.html', {
		'stumpy_domain': stumpy_domain,
		'my_stumps': my_stumps,
		'recent_stumps_list': recent_stumps_list, 
		'famous_stumps_list': famous_stumps_list,
		'stump_stats_num': stump_stats_num,
		'stump_stats_visits': stump_stats_visits
	})	


@login_required
def iframer(request):
	username = request.user
	my_stumps = stump.objects.filter(cookie__iexact=username).order_by('-id')
	stumpy_domain = smart_str(Site.objects.get_current().domain)
	return render_to_response('stumpy/iframe.html', {
			'stumpy_domain': stumpy_domain,
			'username': username,
			'my_stumps': my_stumps,
		})	

def detail(request,short):
	short_clean = bleach.clean(short)
	thisstump = get_object_or_404(stump,shorturl__contains=short_clean)
	thisstump.hits += 1
	thisstump.save()
	go_url = X.unescape(smart_str(thisstump.longurl))
	return redirect(go_url)


@login_required
def submit(request):
	if request.method == 'GET' and request.GET.has_key('l'):
		stumpy_domain = smart_str(Site.objects.get_current().domain)
		stump_clean = bleach.clean(request.GET.get('l'))
		this_stump = smart_str(stump_clean)
		# We shouldn't need the below hack any longer since we now use get method 
		## This code portion is temporary hack for // -> / .... this is a wsgi issue
		#stump_split = list(this_stump.partition(":")) 
		#if stump_split[1] and stump_split[2].startswith("/"):
		#	stump_split[2] = "/"+stump_split[2]
		#	this_stump = ''.join(stump_split)
		this_hash = hashlib.sha1(this_stump).hexdigest()
		does_exist = stump.objects.filter(hashurl=this_hash)
		if not does_exist:
			this_user = smart_str(request.user)
			parsed_url = urlparse.urlparse(this_stump)
			if not parsed_url.scheme:
				this_stump = "http://"+this_stump
			if parsed_url.netloc != stumpy_domain:
				s = stump(longurl=this_stump,hashurl=this_hash,cookie=this_user)
				s.save()
				new_stump = stump.objects.get(id=s.id)	
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
	else:
		return HttpResponse("Sly fox eats the poisoned rabbit.")
