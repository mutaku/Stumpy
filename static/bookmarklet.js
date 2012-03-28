function postUrl(){
		w=window,d=document,t=encodeURIComponent(d.title),link=escape(d.location), 
		w.open(DOMAIN+'/url/?l='+link,'t','status=1,scrollbars=1,location=0,resizable=1,menubar=0,width=200,height=75,toolbar=0'); 
	}
postUrl();
