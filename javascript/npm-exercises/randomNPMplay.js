function dognames(){
const dogNames = require('dog-names');
console.log(dogNames.femaleRandom());
console.log(dogNames.female)
console.log(dogNames.male)
console.log(dogNames.all)
console.log(dogNames.allRandom())
}
// dognames()

function faker(){
const faker = require('faker');
console.log(faker.name.findName())
console.log(faker.internet.email())
console.log(faker.helpers.createCard)
}
// faker()

function wifi(){
  const wifiPassword = require('wifi-password');
  wifiPassword().then(password => {
  	console.log(password);
  });

  const wifiName = require('wifi-name');
  //wifiName() sends a promise for a string with the current wifi name
  wifiName().then(function(name){
    console.log(name);
  });
}
wifi()
