function load_youtube(left_id, left_video_id, right_id, right_video_id){

  var params = { allowScriptAccess: "always" };
  var atts = { id: left_id + "_player" };
  swfobject.embedSWF("http://www.youtube.com/v/" + left_video_id + "?enablejsapi=1&playerapiid=ytplayer&version=3", left_id, "425", "356", "8", null, null, params, atts);

  atts = {id: right_id + "_player" };
  swfobject.embedSWF("http://www.youtube.com/v/" + right_video_id + "?enablejsapi=1&playerapiid=ytplayer&version=3", right_id, "425", "356", "8", null, null, params, atts);
}

function set_song_titles(left_song_title, right_song_title){
  $("#left-song-title").text(left_song_title);
  $("#right-song-title").text(right_song_title);
}

function get_new_battle(){
  $.getJSON( "api/v1/battle/new", function( data ){
    console.log(data);
    left_id = "left_youtube_container";
    left_video_id = data.left_song.song_id;
    right_id = "right_youtube_container";
    right_video_id = data.right_song.song_id;
    load_youtube(left_id, left_video_id, right_id, right_video_id);
    set_song_titles(data.left_song.name, data.right_song.name)
  })
}

function submit_battle_winner(battle_id, winner ){

  $.post( "api/v1/battle/0/winner", { id: battle_id, winner: winner })
    .done(function( data ) {
      console.log(data);
    });

}
