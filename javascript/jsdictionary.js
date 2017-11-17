// Object as Dictionary Exercises

function phonebook(){
  var phonebookDict = {
  Alice: '703-493-1834',
  Bob: '857-384-1234',
  Elizabeth: '484-584-2923'
}
  console.log('print Elizabeths phone number')
  console.log('Elizabeth:', phonebookDict.Elizabeth)
  console.log('Add a entry to the dictionary: Kareems number is 938-489-1234.')
  phonebookDict.Kareem = '938-489-1234'
  console.log(phonebookDict)
  console.log('Delete Alices phone entry.')
  delete phonebookDict.Alice
  console.log(phonebookDict)
  console.log('Change Bobs phone number to 968-345-2345.')
  phonebookDict.Bob = '968-345-2345'
  console.log(phonebookDict)
  var personName = 'Elizabeth'
  for (var attribute in phonebookDict) {
    var value = phonebookDict[attribute];
    console.log(`${attribute}: ${value}`);
  }
};
// phonebook()
function letterHistogram(n){
  var letterDict = {};
  for (let i=0; i<n.length; i++){
    var letter = n[i];
    letterDict[letter] = (letterDict[letter] || 0) + 1;
    //saying, if it returns undefined, set value to default 0 and add 1
  }
  console.log(letterDict)
};

// letterHistogram('bananas')

function wordHistogram(n){
  var wordDict = {};
  words = n.split(' ')
  for (let i=0; i<words.length; i++){
    var word = words[i];
    wordDict[word] = (wordDict[word] || 0) + 1;
    //saying, if it returns undefined, set value to default 0 and add 1
  }
  console.log(wordDict)
};

// wordHistogram('to be or not to be')
// wordHistogram('How much wood would a woodchuck chuck if a woodchuck could chuck wood? He would chuck, he would, as much as he could, and chuck as much wood as a woodchuck would if a woodchuck could chuck wood.')


function popularLetters(n){
    var letterDict = {};
    for (let i=0; i<n.length; i++){
      var letter = n[i];
      letterDict[letter] = (letterDict[letter] || 0) + 1;
  }
  // Create items array
  var items = Object.keys(letterDict).map(function(key) {
      return [key, letterDict[key]];
  });

  // Sort the array based on the second element
  items.sort(function(first, second) {
      return second[1] - first[1];
  });
  console.log(items.slice(0, 2));
}
popularLetters('bananas')
