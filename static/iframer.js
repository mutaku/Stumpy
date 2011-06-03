if (typeof jQuery == 'undefined') {
    // http://www.hunlock.com/blogs/Howto_Dynamically_Insert_Javascript_And_CSS
    var jQ = document.createElement('script');
    jQ.type = 'text/javascript';
    jQ.onload = runthis;
    jQ.src = 'http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js';
    document.body.appendChild(jQ);
} else {
    runthis();
}

// Code from: http://www.smashingmagazine.com/2010/05/23/make-your-own-bookmarklets-with-jquery/
function runthis() {
    if ($("#stumpyframe").length == 0) {
            $("body").append("\
            <div id='stumpyframe'>\
                <div id='stumpyframe_veil' style=''>\
                    <p>Loading...</p>\
                </div>\
                <iframe src='http://t04u.be/iframer/' onload=\"$('#stumpyframe iframe').slideDown(500);\">Enable iFrames.</iframe>\
                <style type='text/css'>\
                    #stumpyframe_veil { display: none; position: fixed; width: 100%; height: 100%; top: 0; left: 0; background-color: rgba(255,255,255,.25); cursor: pointer; z-index: 90000; }\
                    #stumpyframe_veil p { color: black; font: normal normal bold 20px/20px Helvetica, sans-serif; position: absolute; top: 50%; left: 50%; width: 10em; margin: -10px auto 0 -5em; text-align: center; }\
                    #stumpyframe iframe { display: none; position: fixed; top: 10%; left: 10%; width: 80%; height: 80%; z-index: 99900; border: 10px solid rgba(0,0,0,1); margin: -5px 0 0 -5px; }\
                </style>\
            </div>");
            $("#stumpyframe_veil").fadeIn(750);
    } else {
        $("#stumpyframe_veil").fadeOut(750);
        $("#stumpyframe iframe").slideUp(500);
        setTimeout("$('#stumpyframe').remove()", 750);
    }
    $("#stumpyframe_veil").click(function(event) {
        $("#stumpyframe_veil").fadeOut(750);
        $("#stumpyframe iframe").slideUp(500);
        setTimeout("$('#stumpyframe').remove()", 750);
    });
}
