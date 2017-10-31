var pgp = require('pg-promise')({});
var Promise = require ('bluebird');
var prompt = require('prompt-promise');
var db = pgp({database: 'albums'});

function promptAgain(){
  prompt('Add another? yes/no >>> ')
    .then(function(val){
      if (val == 'yes'){
        addArtist();
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
function addArtist(){
var artist = {}
prompt('artist_name: ')
  .then(function (val) {
    artist['artist_name'] = val
    console.log(artist)
    prompt.done();
  })
  .then(function(){
    var q = "INSERT INTO artists \
      VALUES (default, ${artist_name})";
    db.result(q, artist)
      .then(function(result){
        console.log(result)
      })
      .then(function(){
        var query = 'SELECT * FROM artists WHERE artist_name = ${artist_name}'
        db.one(query, artist)
          .then(function(r){
            console.log('Created artist with ID: ',r.id)
            promptAgain();
          })
          .catch(function(err){
            console.log(err)
          })
      })
      .catch(function(err){
        console.log('DB ERROR', err)
      })
    // console.log('Created artist with ID:');
  })
  .catch(function(err){
    console.log('PROMPT ERROR: ', err)
  })
}

addArtist();
