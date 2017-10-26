var index = require('./index')

index.request('https://www.npmjs.com/', function(error, response, body){
  console.log('error: ', error);
  console.log('statusCode:', response && response.statusCode);
  const $ = index.cheerio.load(body);
  var contents = $('a','#pane-frequently-installed').text()
  var y = index.lodash.split(contents, " ")//splits
  var z = index.lodash.compact(y)//removes splaces
  var x = index.lodash.remove(z, function(shit){
    return shit === '\n'})//removes new lines
  // console.log(z)

//trying to slice word up to index of integer
//fail
  for (i = 0; i < z.length; i++) {
    for (j = 0; j < 20; j++){
      let word = z[i]
      if (Number.isInteger(j)== true && word.indexOf(j)!== -1){
        console.log(word.indexOf(j))
      }
    }
  }

});
