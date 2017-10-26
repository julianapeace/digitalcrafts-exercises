//import readline library for js user input function
var fs = require('fs');
var readline = require('readline');
var dns = require('dns');

function readafile(){
//initialize the interface
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
//takes in the question
rl.question("File name: ", function(filename) {
  fs.readFile(filename, function (error, buffer) {
    if (error) {
      console.error(error.message);
      return;
    }
    console.log('File Data: ', buffer.toString());
  });
  rl.close();
});
}
// readafile()

function dnslookup(){
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Domain name: ", function(domainname) {
  dns.lookup(domainname, function (error, buffer) {
    if (error) {
      console.error(error.message);
      return;
    }
    console.log('IP Address: ', buffer.toString());
  });
  rl.close();
});
}
// dnslookup()

function readandwrite(){
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Infile: ", function(infile) {
  console.log(infile)
  //do something with infile

  rl.question("outfile: ", function(outfile){
    //////////////
    console.log(`infile is ${infile}. outfile is ${outfile}`);

    fs.readFile(infile, function(error, buffer){
      if (error){
        console.error(error.message);
        return;
      }
      var contents = buffer.toString();
      var upper = contents.toUpperCase();
      console.log(upper)

      fs.writeFile(outfile, upper, function(error){
        if (error){
          console.error(error.message);
          return;
        }
        console.log('File Saved: ', outfile)
      })
    })

    rl.close();
    //////////////
  });
});
}
readandwrite()
