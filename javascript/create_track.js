var pgp = require('pg-promise')({});
var Promise = require ('bluebird');
var prompt = require('prompt-promise');
var db = pgp({database: 'albums'});

function promptAgain(){
  prompt('Add another? yes/no >>> ')
    .then(function(val){
      if (val == 'yes'){
        addTrack();
      }
      else if (val == 'no'){
        pgp.end();
        process.exit();
      }
      else{
        console.log('Invalid Input')
        console.log('Try Again')
        promptAgain();
      }
    })
    .catch(function(err){
      console.log('PROMPT AGAIN ERROR: ', err)
    })
}

function addTrack(){
  var track = {}
  prompt('track_name: ')
    .then(function (val) {
      track['track_name'] = val
      return prompt('track_duration: ');
    })
    .then(function(val){
      track['track_duration'] = val
      return prompt('Album ID: ')
    })
    .then(function(val){
      track['tracks_album_ID_fkey'] = parseInt(val)
      prompt.end();
    })
    .then(function(){
      var query = "INSERT INTO tracks \
          VALUES (default, ${track_name}, ${tracks_album_ID_fkey}, ${track_duration})";
      db.result(query, track)
        .then(function(result){
          console.log(result)
          var q = "SELECT * FROM tracks WHERE track_name = ${track_name}"
          db.one(q, track)
            .then(function(r){
              console.log('Created Track with ID: ', r.id)
              promptAgain();
            })
            .catch(function(e){
              console.log(e)
            })
        })
        .catch(function(err){
          console.log('DB ERROR: ',err)
        })
    })
}
addTrack();
