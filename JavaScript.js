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