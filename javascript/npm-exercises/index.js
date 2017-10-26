var marked = require('marked');
var lodash = require('lodash');
var request = require('request');
var emojione = require('emojione');
var string = require('string');
var cheerio = require('cheerio');


function marked (){
  marked.setOptions({
      renderer: new marked.Renderer(),
      gfm: true,
      tables: true,
      breaks: false,
      pedantic: false,
      sanitize: false,
      smartLists: true,
      smartypants: false
    });

  console.log(marked('I am using __markdown__.'));
  console.log(marked('# Marked in browser\n\nRendered by **marked**.'));
}
// marked()
function lodash(){
  var array = ['a', 'b', 'c', 'd']
  console.log(lodash.chunk(array, [size=2]));
  console.log(lodash.shuffle(array));
  console.log(lodash.random(1,100, false))
}
// lodash()

function request(){
  request('https://getmypup.com', function (error, response, body) {
    console.log('error:', error); // Print the error if one occurred
    console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
    console.log('body:', body); // Print the HTML for the Google homepage.
  });
};
// request()

function apirequest(){
var options = {
  url: 'https://api.github.com/repos/request/request',
  headers: {
    'User-Agent': 'request'
  }
};

function callback(error, response, body) {
  if (!error && response.statusCode == 200) {
    var info = JSON.parse(body);
    console.log(info)
    console.log(info.stargazers_count + " Stars");
    console.log(info.forks_count + " Forks");
    //found emoji in request
    var x = info.description + " Description";
    //isolated emoji
    var emoji = lodash.split(x, " ").slice(0,1)[0];
    //trying to get it to convert to utf16 surrogate pairs
    console.log(emoji)
    var result = emoji.charCodeAt();
    console.log(result)
    console.log(String.fromCharCode(parseInt(result, 16)));
    console.log("😸".codePointAt(0))
  }
}

request(options, callback);
};
apirequest()

function emojifun(){
var emoji = "🦄";
var shortname = emojione.toShort(emoji);
console.log(shortname)

var shortnametoimage = emojione.shortnameToImage(shortname)
console.log(shortnametoimage) //converts to html img tag

var image = emojione.toImage(shortname)
console.log(image) //converts to html img tag
}
// emojifun()

//////////////////////
///////exports////////
//////////////////////
exports.marked = marked;
exports.lodash = lodash;
exports.request = request;
exports.cheerio = cheerio;
