function add(x, y) {
  var result = x + y;
  return result;
}

function subtract(x, y) {
  return x - y;
}

function greeting(person) {
  return 'Hola, ' + person + '!';
}

function product(numbers) {
  return numbers.reduce(function(a, b) {
    return a * b;
  }, 1);
}
///////////////////////////////////////////
//
//            CALLBACK FUNC
//
///////////////////////////////////////////
function add (x, y, callback) {
  var result = x + y;
  callback(result);
}
add(1, 2, function (result) { console.log(result); });

function subtract(x, y, callback){
  var result = x - y;
  callback(result);
}
subtract(2, 1, function(result) {console.log(result); });

function greeting(person, callback) {
  var result = 'Hola, ' + person + '!';
  callback(result)
}
greeting('Julie', function(result) {console.log(result);})

//numbers is looking for a list of numbers like [3, 4, 1, 2]
function product(numbers, callback) {
  var result = numbers.reduce(function(a, b) {
    return a * b;
  }, 1);
  callback(result)
}
product([3,4,1,2], function(result) {console.log(result)})
