/*
 * Programming Quiz: JuliaJames (4-1)
 */

var x = 1;

while (x<21) {
    // check divisibility
    // print Julia, James, or JuliaJames
    // increment x
    if(x%3===0){
        console.log("Julia")
    }else if(x%5===0){
        console.log("James")
    }else if(x%3===0 && x%15===0){
        console.log("JuliaJames")
    }else{
        console.log(x)
    }
    
    x=x+1
    
}



/*
 * Functions
 */
// function expression catSays
var catSays = function(max) {
  var catMessage = "";
  for (var i = 0; i < max; i++) {
    catMessage += "meow ";
  }
  return catMessage;
};

// function declaration helloCat accepting a callback
function helloCat(callbackFunc) {
  return "Hello " + callbackFunc(3);
}

// pass in catSays as a callback function
helloCat(catSays);



/*
 * Programming Quiz: Another Type of Loop (6-8)
 *
 * Use the existing `test` variable and write a `forEach` loop
 * that adds 100 to each number that is divisible by 3.
 *
 * Things to note:
 *  - you must use an `if` statement to verify code is divisible by 3
 *  - you can use `console.log` to verify the `test` variable when you're finished looping
 */

var test = [12, 929, 11, 3, 199, 1000, 7, 1, 24, 37, 4,
    19, 300, 3775, 299, 36, 209, 148, 169, 299,
    6, 109, 20, 58, 139, 59, 3, 1, 139
];

// Write your code here
test.forEach(function(num){
    if(num%3===0){
        num+=100
    }
});

console.log(test)


// addEventListener
const lotsOfElements = document.querySelectorAll('.quizzing-quizzby');
const element = lotsOfElements[2];

element.addEventListener('animationend', function () {
    const mainHeading = document.querySelector('h1');

    mainHeading.style.backgroundColor = 'purple'; 
});