//in the brackets this is where you can put some options in
var pgp = require('pg-promise')({});
//by default will use Node's promise feature. If you want the finally statement, use bluebird.
var Promise = require ('bluebird');
//point to your postgres database
var db = pgp({database: 'restaurant'});
//pass in SQL statements
db.query('SELECT * FROM restaurant')
  .then(function(results){
    results.forEach(function(r){
      console.log(r.id, r.name);//can access like an object
    })
  })
  .catch(function(error){
    console.log(error);
  });
//everytime you do a query, you get a promise.bc its pgp.

//QUERY METHODS
// one: expects one row or errors out
// any: no expectations
// none: expects no result or error
// many: expects one or more rows or error
// result: return the raw results, useful for insert update, and deletes

db.one('SELECT * FROM restaurant WHERE id = 1')
  .then(function(r){
    console.log(r.id, r.name)
  })
  .catch(function(error){
    console.log(error)
  })

//get a simple result back. if you don't care about the details, just want to know if you successfully inserted.
db.result("INSERT INTO restaurant \
  VALUES (default, 'Narf')")
  .then(function (result) {
    console.log(result);
  });

//var name is picked up from the front end, anything the user inputs.
var name = "Big Belly Burger";
var query = `INSERT INTO restaurant \
  VALUES (default, '${name}')`;
db.result(query)
  .then(function (result) {
    console.log(result);
  })
  .catch(function(err){
    console.log(err);
  });
//doing var name this way exposes you to SQL injection
//var name = "Big Belly Burger'; DROP TABLE restaurant; --";
//Better way to get var name
//converts input into a string, automatically escapes spaces. dont do it yourself you'll mess up
var name = "Big Belly Burger'; DROP TABLE restaurant; --";
var query = `INSERT INTO restaurant \
  VALUES (default, $1)`;//1 means the first argument. if it is $2, you can add category nxt to query, name, category
db.result(query, name)//this is the line thats doing the sanitizing
  .then(function (result) {
    console.log(result);
  })
  .catch(function(err){
    console.log(err);
  });
//can insert objects instead of strings
var biz = {name: "Lard Lad Donuts"};
var q = "INSERT INTO restaurant \
  VALUES (default, ${name})";
db.result(q, biz)
  .then(function (result) {
    console.log(result);
  });

//after you're done with db opps, you need to close the connection. node will automatically clean it up if you don't do anything for a while, but you'll like to add this script to clean it up.
pgp.end()
