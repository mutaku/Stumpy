if (typeof jQuery == 'undefined') {
    var jQ = document.createElement('script');
    jQ.type = 'text/javascript';
    jQ.onload = runthis;
    jQ.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js';
    document.body.appendChild(jQ);
} else {
    runthis();
}

function closer() {
	$("#stumpyframe_veil").fadeOut(750);
	$("#stumpyframe iframe").animate({width:'toggle'},350);
	setTimeout("$('#stumpyframe').remove()", 750);
}

function runthis() {
// script modified from : http://iamnotagoodartist.com/stuff/wikiframe.js
	if ($("#stumpyframe").length == 0) {
		$("body").append("\
			<div id='stumpyframe'>\
				<div id='stumpyframe_veil' style=''>\
					<p>Harvesting your Stumps! ...</p>\
				</div>\
				<iframe src='http://t04u.be/iframer/' onload=\"$('#stumpyframe iframe').animate({width:'toggle'},500);$('#stumpyframe_veil p').hide(500);\">Enable iFrames.</iframe>\
				<style type='text/css'>\
					#stumpyframe {z-index: 850;}\
					#stumpyframe_veil { display: none; position: fixed; width: 100%; height: 100%; top: 0; left: 0; cursor: pointer; z-index: 900; }\
					#stumpyframe_veil p { color: black; font: normal normal bold 20px/20px Helvetica, sans-serif; position: absolute; top: 50%; left: 50%; width: 28em; margin: -10px auto 0 -5em; text-align: center; }\
					#stumpyframe iframe { display: none; position: fixed; top: 0; left: 0; width: 50em; height: 100%; z-index: 999; border: 10px solid #ccc; background: white; margin: -5px 0 0 -5px; }\
				</style>\
			</div>");
			$("#stumpyframe_veil").fadeIn(500);
	} else { closer(); }

	$("#stumpyframe_veil").click(function(event){
		closer();
	});
}
