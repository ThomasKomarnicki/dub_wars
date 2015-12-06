function load_youtube(left_id, left_video_id, right_id, right_video_id){

  var params = { allowScriptAccess: "always" };
  var atts = { id: left_id + "_player" };
  swfobject.embedSWF("http://www.youtube.com/v/" + left_video_id + "?enablejsapi=1&playerapiid=ytplayer&version=3", left_id, "425", "356", "8", null, null, params, atts);

  atts = {id: right_id + "_player" };
  swfobject.embedSWF("http://www.youtube.com/v/" + right_video_id + "?enablejsapi=1&playerapiid=ytplayer&version=3", right_id, "425", "356", "8", null, null, params, atts);
}

function change_yt_songs(left_video_id, right_video_id){
  left_yt_player = get_left_yt_player();
  right_yt_player = get_right_yt_player();

  left_yt_player.cueVideoByUrl({
    mediaContentUrl:"http://www.youtube.com/v/" + left_video_id + "?enablejsapi=1&playerapiid=ytplayer&version=3",
  });
  right_yt_player.cueVideoByUrl({
    mediaContentUrl:"http://www.youtube.com/v/" + right_video_id + "?enablejsapi=1&playerapiid=ytplayer&version=3",
  });

  // left_yt_player.pauseVideo();
  // right_yt_player.pauseVideo();
}

function set_song_titles(left_song_title, right_song_title){
  $("#left-song-title").text(left_song_title);
  $("#right-song-title").text(right_song_title);
}

function left_song_select(){
  submit_battle_winner(current_battle_id, 1);
}

function right_song_select(){
  submit_battle_winner(current_battle_id, 2);
}



function get_left_yt_player(){
  player = document.getElementById("left_youtube_container_player");
  // player = new YT.Player('left_youtube_container_player', {
  //   events: {
  //     // 'onReady': onPlayerReady,
  //     // 'onStateChange': onPlayerStateChange
  //   }
  // });
  return player;
}

function get_right_yt_player(){
  player = document.getElementById("right_youtube_container_player");
  // player = new YT.Player('right_youtube_container_player', {
  //   events: {
  //     // 'onReady': onPlayerReady,
  //     // 'onStateChange': onPlayerStateChange
  //   }
  // });
  return player;
}
