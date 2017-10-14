var deck = [
  { point: 13, suit: 'hearts' },
  { point: 12, suit: 'hearts' },
  { point: 11, suit: 'hearts' },
  { point: 10, suit: 'hearts' },
  { point: 9, suit: 'hearts' },
  { point: 8, suit: 'hearts' },
  { point: 7, suit: 'hearts' },
  { point: 6, suit: 'hearts' },
  { point: 5, suit: 'hearts' },
  { point: 4, suit: 'hearts' },
  { point: 3, suit: 'hearts' },
  { point: 2, suit: 'hearts' },
  { point: 1, suit: 'hearts' },
  { point: 13, suit: 'diamonds' },
  { point: 12, suit: 'diamonds' },
  { point: 11, suit: 'diamonds' },
  { point: 10, suit: 'diamonds' },
  { point: 9, suit: 'diamonds' },
  { point: 8, suit: 'diamonds' },
  { point: 7, suit: 'diamonds' },
  { point: 6, suit: 'diamonds' },
  { point: 5, suit: 'diamonds' },
  { point: 4, suit: 'diamonds' },
  { point: 3, suit: 'diamonds' },
  { point: 2, suit: 'diamonds' },
  { point: 1, suit: 'diamonds' },
  { point: 13, suit: 'clubs' },
  { point: 12, suit: 'clubs' },
  { point: 11, suit: 'clubs' },
  { point: 10, suit: 'clubs' },
  { point: 9, suit: 'clubs' },
  { point: 8, suit: 'clubs' },
  { point: 7, suit: 'clubs' },
  { point: 6, suit: 'clubs' },
  { point: 5, suit: 'clubs' },
  { point: 4, suit: 'clubs' },
  { point: 3, suit: 'clubs' },
  { point: 2, suit: 'clubs' },
  { point: 1, suit: 'clubs' },
  { point: 13, suit: 'spades' },
  { point: 12, suit: 'spades' },
  { point: 11, suit: 'spades' },
  { point: 10, suit: 'spades' },
  { point: 9, suit: 'spades' },
  { point: 8, suit: 'spades' },
  { point: 7, suit: 'spades' },
  { point: 6, suit: 'spades' },
  { point: 5, suit: 'spades' },
  { point: 4, suit: 'spades' },
  { point: 3, suit: 'spades' },
  { point: 2, suit: 'spades' },
  { point: 1, suit: 'spades' },
];

function getCardImageURL(x){
  if (deck[x]['point']==13){
    var card = 'king' + "_of_" + deck[x]['suit'] + ".png"
  }else if(deck[x]['point']==1){
    var card = 'ace' + "_of_" + deck[x]['suit'] + ".png"
  }else if(deck[x]['point']==11){
    var card = 'jack' + "_of_" + deck[x]['suit'] + ".png"
  }else if(deck[x]['point']==12){
    var card = 'queen' + "_of_" + deck[x]['suit'] + ".png"
  }else{
  var card = deck[x]['point'] + "_of_" + deck[x]['suit'] + ".png"
  };
  deck.splice(x,1);
  return card;
};

function calculatePoints(n){
  total = 0
  for(let i=0; i<n.length; i++){
    total = total + n[i]
  }
  return total;
};

function shuffleArray(array) {
  for (var i = array.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var temp = array[i];
      array[i] = array[j];
      array[j] = temp;
  }
  return array;
}
var dealerHand = []
var playerHand = []

$(document).ready(function () {
 console.log('printed')
 $('#deal-button').click(function(event){
   card = 1
   dealerHand.push(deck[card])
   let x = getCardImageURL(card);
    $('#dealer-hand').append('<img src="/images/'+ x + '" />');
    var points = calculatePoints(dealerHand)
    $('#dealer-points').text(points)

 })
 $('#hit-button').click(function(event){
   var card = $('<img src="/images/7_of_clubs.png" alt="">')
   $('#dealer-hand').append(card)
 })
});


//deck.splice(2,1) to remove card from deck
