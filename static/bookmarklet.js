// bookmarklet to submit urls to stumpy
//	domain is hardcoded here - you must change that.
function(){
		w=window,
		d=document,
		t=encodeURIComponent(d.title),
		l=escape(d.location), 
		w.open(
				'http://t04u.be/url/'+l,
				't',
				'status=1,
				scrollbars=1,
				location=0,
				resizable=1,
				menubar=0,
				width=200,
				height=75,
				toolbar=0'
			); 
	})();
