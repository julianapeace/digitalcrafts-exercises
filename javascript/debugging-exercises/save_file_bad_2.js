/*

Running this file reports that it saves the file, when in reality it does not.

JULIE FIXED! line 15 tried to place the file into a non-existing directory. need to npm install var mkdirp = require('mkdirp'); it will create directories that don't exist--well exist.
*/
var request = require('request-promise');
var fs = require('fs-promise');
var mkdirp = require('mkdirp');

var url = 'https://davidwalsh.name/'
request.get(url)
  .then(function(html) {
    fs.writeFile('data/davidwalsh.html', html, function(err){console.log(err)});
  })
  .then(function() {
    console.log('Wrote file data/davidwalsh.html');
  })
  .catch(function(err) {
    console.log('Something went wrong');
    console.log(err.message);
  });
