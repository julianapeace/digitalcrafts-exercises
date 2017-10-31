/*
Running this file shows an error, but the error is not catch by the catch block in the promise chain, as is evidenced by the fact that the sentence "Something went wrong" is not displayed.
*/

var request = require('request-promise');
var fs = require('fs');

var mkdirp = require('mkdirp');

mkdirp('/tmp/foo/bar/baz', function (err) {
    if (err) console.error(err)
    else console.log('pow!')
});

var amjad = 'https://amasad.me/';
var filename = 'amjad.html';
var path = './data';

request.get(amjad)
  .then(function(html) {
    var contents = html.toUpperCase();
    fs.mkdir(path, function (err) {
        if (err) {
            console.log('failed to create directory', err);
        } else {
            fs.writeFile(path + "/amjad.html", contents, function(err) {
                if (err) {
                    console.log('error writing file', err);
                } else {
                    console.log('writing file succeeded');
                }
            });
        }
    });
    // return fs.writeFile('data/amjad.html', contents, function(err){console.log(err)});
  })
  .then(function() {
    console.log('Wrote file ' + filename);
  })
  .catch(function(err) {
    console.log('Something went wrong');
    console.log(err.message);
  });
