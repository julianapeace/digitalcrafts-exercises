
function madlibs(name, subject) {
  var output = '%s favorite subject in school is %s';
  console.log(output, name, subject);
  return output;
}
// madlibs('Julie', 'computer science')

function tipcalculator(bill, service){
  if (service == 'good'){
    service = .2;
  }else if (service=='fair'){
    service = .15;
  }else{
    service = .1;
  }
  let output = bill + (bill * service);
  console.log(output);
  return output;
}
// tipcalculator(100, 'good')

function printNumbers(x, y){
  for (var count=x; count < y+1; count++) {
    console.log(count);
  }
}
// printNumbers(1,10)
function printNumbersWhile(x, y){
  count = x-1;
  while(count < y){
    count += 1;
    console.log(count);
  }
}
// printNumbersWhile(1,10)

function printSquare(i){
  for (var count=0; count < i; count++) {
    console.log('*'.repeat(i));
  }
}
// printSquare(5)

function printBox(i,j){
  for (var count=0; count < j; count++) {
    if (count == j-1 || count == 0){
      console.log('*'.repeat(i));
    }else{
      console.log('*' + " ".repeat(i-2) + '*');
    }
  }
}
// printBox(6,4)

function printBanner(i){
  let long = i.length + 2
  console.log('*'.repeat(long));
  console.log('*'+ i + '*')
  console.log('*'.repeat(long));
}
// printBanner(' Welcome to DigitalCrafts ')

function leetspeak(i){
  string = i.toLowerCase()
  long = string.length
  myArray = []
  for (var count=0; count < long; count++) {
    myArray.push(string[count])
  }
  for (var count=0; count < long; count++) {
    if (myArray[count]== 'a'){
      myArray[count]=4;
    }else if(myArray[count] == 'e'){
      myArray[count]=3;
    }else if(myArray[count] == 'g'){
      myArray[count]=6;
    }else if(myArray[count] == 'i'){
      myArray[count]=1;
    }else if(myArray[count] == 'o'){
      myArray[count]=0;
    }else if(myArray[count] == 's'){
      myArray[count]=5;
    }else if(myArray[count] == 't'){
      myArray[count]=7;
    }
  }
  console.log(myArray.join(''))
}
// leetspeak('Leetspeak')

function loongVowels(string){
  var vowels = ['a','e','i','o','u'];
  myArray = [];
  counter = 0;

  for (var i=0; i < string.length; i++) {
    if (vowels.includes(string[i])){
      counter += 1;
    }
    if (counter > 1){
      counter = 0;
      myArray.push(string[i].repeat(3));
    }
    myArray.push(string[i]);
  }
  console.log(myArray.join(''));
}
// loongVowels('Good')

function bePositive(array){
  myArray = []
  for (var i=0; i < array.length; i++) {
    if (array[i] > -1){
      myArray.push(array[i])
    }
  }
  console.log(myArray)
}
// bePositive([1, -3, 5, -3, 0])
