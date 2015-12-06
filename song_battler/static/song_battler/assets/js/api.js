function load_initial_battle(){
  $.getJSON( "api/v1/battle/new", function( data ){
    current_battle_id = data.id;
    left_id = "left_youtube_container";
    left_video_id = data.left_song.song_id;
    right_id = "right_youtube_container";
    right_video_id = data.right_song.song_id;
    load_youtube(left_id, left_video_id, right_id, right_video_id);
    set_song_titles(data.left_song.name, data.right_song.name)
  });
}

function get_new_battle(){
  $.getJSON( "api/v1/battle/new", function( data ){
    console.log(data);
    change_yt_songs();
    current_battle_id = data.id;
    // left_id = "left_youtube_container";
    left_video_id = data.left_song.song_id;
    // right_id = "right_youtube_container";
    right_video_id = data.right_song.song_id;
    // load_youtube(left_id, left_video_id, right_id, right_video_id);
    set_song_titles(data.left_song.name, data.right_song.name);
    change_yt_songs(left_video_id, right_video_id);
  });
}

function submit_battle_winner(battle_id, winner ){

  endpoint = "api/v1/battle/" + battle_id + "/winner/?format=json"
  $.ajax({
    method: "PUT",
    contentType: "application/json",
    dataType: "json",
    url: endpoint,
    data: { winner: winner }})
    .done(function( data ) {
      console.log("set winner returned");
      console.log(data);
      get_new_battle();
    });

}
