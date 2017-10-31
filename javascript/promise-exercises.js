var rp = require('request-promise');
var Promise = require("bluebird");
var cheerio = require('cheerio');
var lodash = require('lodash');


var urls = [
  'https://en.wikipedia.org/wiki/Futures_and_promises',
  'https://en.wikipedia.org/wiki/Continuation-passing_style',
  'https://en.wikipedia.org/wiki/JavaScript',
  'https://en.wikipedia.org/wiki/Node.js',
  'https://en.wikipedia.org/wiki/Google_Chrome'
];

Promise.all(urls)
  .then(response =>{
  rp(response)
  .then(function(html){
    console.log(html)
  })
  .catch(function(err){
    console.log('error'+err)
  })
})
  .catch(function(err){
    console.error('Error' + err);
  });
