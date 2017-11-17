const express = require('express')
const app = express()
const importEnv = require('import-env')
const port = process.env.PORT || 8000;
const body_parser = require('body-parser');
var axios = require('axios')
app.use(body_parser.urlencoded({extended: false}));

app.set('view engine', 'hbs');
app.use(express.static('public'));

app.get('/', function(req, res){
  res.render('index.hbs');
});

app.post('/api', function(req,res){


  var api_url = 'https://api.darksky.net/forecast/5da02e8833bd1009ad0a6cbb58770bf8/29.7431508,-95.38871999999999';
  axios.get(api_url)
    .then(function (response) {
      var summary = response.data.currently.summary;
      var temp = response.data.currently.temperature;
      var windSpeed = response.data.currently.windSpeed;
      var visibility = response.data.currently.visibility;
      var array = [summary, temp, windSpeed, visibility]
      res.render('index.hbs',{'array':array})
      // return response
    })
    .catch(function (error) {
      console.error(error);
    });
  })

app.post('/myapi', function (req, res) {
    var api_url = 'http://localhost:8000/api';
    axios.get(api_url)
      .then(function (response) {
        console.log(response)
        res.json(
          {message: 'This is an API Chump!'}
        );
      })
      .catch(function (error) {
        console.error(error);
      });
});

app.listen(port, function(){
  console.log('listening on port ' + port)
});
