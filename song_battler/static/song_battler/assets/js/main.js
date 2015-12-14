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
  return player;
}

function get_right_yt_player(){
  player = document.getElementById("right_youtube_container_player");
  return player;
}

function get_home_list_yt_player(){
  player = document.getElementById("list-youtube-current-inner");
  return player;
}

function pause_home_list_yt_player(){
  yt_player = get_home_list_yt_player();
  if(yt_player != null){
    yt_player.pauseVideo();
  }
}

function on_list_item_play(){
// todo
  button = $(event.target);
  $(".list-youtube-holder").removeClass("visible");
  pause_home_list_yt_player();
  if(button.hasClass("opened")){
    // close
    button.removeClass("opened");

  }else{
    // open
    $(".play-button").removeClass("opened");
    button.addClass("opened");
    var list_youtube_holder = button.parent().children(".list-youtube-holder").eq(0);
    list_youtube_holder.addClass("visible");

    addYoutubeToListHolder(list_youtube_holder);

  }

}

function addYoutubeToListHolder(list_youtube_holder){
  $(".list-youtube-holder-inner").removeAttr("id");
  list_youtube_holder.children(".list-youtube-holder-inner").attr('id', 'list-youtube-current');
  video_id = list_youtube_holder.attr("data-video-id");

  var params = { allowScriptAccess: "always" };
  var atts = { id: "list-youtube-current-inner" };
  // swfobject.removeSWF("list-youtube-current-inner");
  swfobject.embedSWF("http://www.youtube.com/v/" + video_id + "?enablejsapi=1&playerapiid=ytplayer&version=3", "list-youtube-current", "425", "356", "8", null, null, params, atts);
}

function onHomeScroll(){
  var scroll = document.body.scrollTop;
  console.log("scroll = " + scroll);
  // todo
  $(".large-background").css("top", 0-(scroll/4));
}
