/*

WTF?

Running this script file not only doesn't create the promise.html file it is supposed to, but it prints out this giant blob of HTML.

*/
/*
JULIE SOLVED IT! checked fs.writeFile docs. Line 19, deleted third argument - 'buffer'.
*/

var request = require('request-promise');
var fs = require('fs-promise');

var url = 'https://en.wikipedia.org/wiki/Futures_and_promises'
request.get(url)
  .then(function(buffer) {
    var contents = buffer.toString().toUpperCase();
    return fs.writeFile('promise.html', contents);
  })
  .then(function() {
    console.log('Wrote file promise.html');
  })
  .catch(function(err) {
    console.log('Something went wrong');
    console.log(err.message);
  });
