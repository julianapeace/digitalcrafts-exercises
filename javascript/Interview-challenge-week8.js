///////////////////////////////
// Week8 interview challenge//
/////////////////////////////
Challenge 1
/////////////////////////////
Design a web application that is a Twitter clone. Describe the URLs and what each URL does like the ToDo App exercise. The app should be able to post a message, follow other users, view my list of messages and the people I follow, and view a list of messages from another user.

This is a non-coding challenging. You only need to create the specification of what you want built. Imagine your the manager and you need to describe what needs to be built to other developers.

Schema -
/ - home page: login page. If cookie says you've already logged in, the page populates with list of tweets from your list of tweeters you are "following". There is a text input field at the top with a submit button /submitNewTweet. The button next to existing tweets is the button to /retweet and /follow

/submitNewTweet - takes the text input and stores it in your personal database with your user info and a timestamp. It is now linked to you.

/retweet - takes the tweet text and copies it into your database with your username along with the original tweeters info.

/follow - adds the tweeters user id into your personal database of "following".

/profile - In the navbar, you can view your personal profile which loads with a query of your personal database. it shows you all your tweets and who you are following.
/////////////////////////////
Challenge 2
/////////////////////////////
Given a list of numbers find the number of pairs that add to 0. Numbers are unique and will not repeat.

Example: [-2, 1, 0, 2] => 1 pair since only -2 + 2 = 0

function x(array){
  let counter = 0
  for (i = 0; i < array.length; i++){
      if (i + 1 === array.length){
        //because 3 + 1 = 4 and index(4) does not exist. Will come back undefined.
        break
      }
      else if (array[i] + array[i+1] === 0){
        counter += 1
    }
  }
  return counter
}


/////////////////////////////
Challenge 2b
/////////////////////////////
What is the Big O complexity of your answer? If your algorithm is greater than O(n) then write an algorithm that has a computational complexity of O(n).

According to this sheet: http://bigocheatsheet.com/
my answer is O(n).
/////////////////////////////
Challenge 3
/////////////////////////////
Write a Bozo sort algorithm, not to be confused with the slightly less efficient bogo sort, consists out of checking if the input sequence is sorted and if not swapping randomly two elements. This is repeated until eventually the sequence is sorted.

bogosort is randomly sorting all the elements until it is sorted. Big O complexity of O(n!), super inefficient.

bozo is slightly less inefficient because it swaps two random elements until it is sorted. Still O(n!).

import random
function is_sorted(array){
  for (i = 0; i < array.length; i++){
    if (i + 1 === array.length){
      //because 3 + 1 = 4 and index(4) does not exist. Will come back undefined.
      break
    }
    else {
      array[i] < array[i+1]
      return true
    }
  }
}

function bozosort(array){
    if (is_sorted(array) === true){
      break
    }
    else{
      let firstNum = array[randomInt]
      let secondNum = array[randomInt]

      let temp = firstNum
      firstNum = secondNum
      secondNum = temp
      bozosort(array)//recursive or infinite loop?
    }
}
/////////////////////////////
Challenge 4
/////////////////////////////
In a room N chairs are placed around a round table. Knights enter the room one by one and choose at random an available empty chair. To have enough elbow room the knights always leave at least one empty chair between each other. When there arent any suitable chairs left, the fraction C of empty chairs is determined.

We also define E(N) as the expected value of C. We can verify that E(4) = 1/2 and E(6) = 5/9. Find E(1018).

Give your answer rounded to fourteen decimal places in the form 0.abcdefghijklmn.
.125
.0925
