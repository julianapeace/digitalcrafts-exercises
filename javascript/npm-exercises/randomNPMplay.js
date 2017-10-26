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

const wifiPassword = require('wifi-password');

wifiPassword().then(password => {
	console.log(password);
});
