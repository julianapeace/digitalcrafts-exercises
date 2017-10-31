////////////ALBUM exercises
var pgp = require('pg-promise')({});
var Promise = require ('bluebird');
var prompt = require('prompt-promise');
var db = pgp({database: 'albums'});

function promptAgain(){
  prompt('Add another? yes/no >>> ')
    .then(function(val){
      if (val == 'yes'){
        addAlbum();
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
function addAlbum(){
var album = {}
prompt('album_name: ')
  .then(function (val) {
    album['album_name'] = val
    return prompt('album_year: ');
  })
  .then(function (val) {
  album['album_year'] = parseInt(val)
  return prompt('artist_ID: ')
  })
  .then(function(val){
    album['albums_artist_ID_fkey'] = parseInt(val)
    console.log(album)
    prompt.done();
  })
  .then(function(){
    var query = "INSERT INTO albums \
        VALUES (default, ${album_name}, ${album_year}, ${albums_artist_ID_fkey})";
    db.result(query, album)
      .then(function(result){
        console.log(result);
      })
      .then(function(){
        var q = "SELECT * FROM albums WHERE album_name = ${album_name}";
        db.one(q, album)
          .then(function(r){
            console.log('created album with ID: ',r.id);
            promptAgain();
          })
          .catch(function(err){
            console.log(err)
          })
      })
      .catch(function(err){
        console.log('DB ERROR:', err.stack)
      })
  })
  .catch(function rejected(err) {
    console.log('PROMPT error:', err.stack);
    prompt.finish();
  });
}

addAlbum();
