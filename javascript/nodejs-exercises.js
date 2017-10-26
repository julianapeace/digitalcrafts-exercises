//import readline library for js user input function
var readline = require('readline');
//initialize the interface
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
//takes in the question
rl.question("File name", function(answer) {
  console.log("Awesomesauce:", answer);
  rl.close();
});
