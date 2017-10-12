function evenNum(n){
  console.log('Write a function which takes an array of numbers as input and returns a new array containing only the even numbers in the given array.')
  var array = []
  n.forEach(function(num){if (num%2==0){array.push(num)}});
  console.log(array)
};
// evenNum([1,2,3,4])

function squareNum(n){
  console.log('Write a function which takes an array of numbers as input and returns a new array containing result of squaring each of the numbers in the given array by two. Example: squareTheNumbers([1, 2, 3]) should give [1, 4, 9].')
  function test(n){
    return n*n;
  }
  var squared = n.map(test)
  console.log(squared)
};
// squareNum([1,2,3])

var cities = [
  { name: 'Los Angeles', temperature: 60.0},
  { name: 'Atlanta', temperature: 52.0 },
  { name: 'Detroit', temperature: 48.0 },
  { name: 'New York', temperature: 80.0 }
];

function citiesExercise(n){
  console.log('Write a function which takes an array of city objects like such: var cities as input and returns a new array containing the cities whose temperature is cooler than 70 degrees.')
  var array = []
  n.map(function(item){
    if (item.temperature < 70){
      array.push(item);
    }
  })
  console.log(array)
};
// citiesExercise(cities)

var people = [
  'Dom',
  'Lyn',
  'Kirk',
  'Autumn',
  'Trista',
  'Jesslyn',
  'Kevin',
  'John',
  'Eli',
  'Juan',
  'Robert',
  'Keyur',
  'Jason',
  'Che',
  'Ben'
];

function goodJob(n){
  console.log('Given an array of people\'s names: Print out "Good Job, {{name}}!"" for each person\'s name, one on a line.')
  n.forEach(function(name){console.log('Good Job'+ " " + name)})
};
// goodJob(people);

function sortArray(n){
  console.log('Given an array of strings such the array of names given in the previous problem, sort them by alphabetically order.')
  console.log(n.sort())
};
// sortArray(people)

function sortArray2(n){
  console.log('Sort the same array, but not by alphabetically order, but by how long each name is, shortest name first.')
  console.log(n.sort(function(x,y){
  if (x.length>y.length){return 1}
  else if (x.length<y.length){return -1}
  return 0;
  }))
};
// sortArray2(people)

function fun(){console.log('Hello, World!')};
function call3Times() {
  console.log('Given this function: Use the call3Times function to print "Hello, world!" 3 times.')

  fun();
  fun();
  fun();
}
// call3Times()

function callNTimes(n, x){
  console.log('You will write a function callNTimes that takes two arguments: times as a number, and fun as a function. It will call that function for that many times.You are allowed to use a loop in the implementation of callNTimes.')
  for (var i=0; i<n; i++) {fun(i)};
};
function hello(){console.log('Hello, World!')};
var hello = hello();
// callNTimes(5, hello)

function acronym(n){
  console.log('Write a function acronym that takes an array of words as argument and returns the acronym of the words. Use the reduce method to do this.')
  function test (sum, value){return sum + value[0];};
  console.log(n.reduce(test, "").toUpperCase())
};
// acronym(['very', 'important', 'person'])
// acronym(['national', 'aeronautics', 'space', 'administration'])
