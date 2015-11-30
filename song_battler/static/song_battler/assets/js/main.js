function load_youtube(left_id, left_video_id, right_id, right_video_id){

  var params = { allowScriptAccess: "always" };
  var atts = { id: left_id + "_player" };
  swfobject.embedSWF("http://www.youtube.com/v/" + left_video_id + "?enablejsapi=1&playerapiid=ytplayer&version=3", left_id, "425", "356", "8", null, null, params, atts);

  atts = {id: right_id + "_player" };
  swfobject.embedSWF("http://www.youtube.com/v/" + right_video_id + "?enablejsapi=1&playerapiid=ytplayer&version=3", left_id, "425", "356", "8", null, null, params, atts);
}

$(window).ready(function(){
  $.getJSON( "api/v1/battle/new", function( data ){
    console.log(data);
  })

})
