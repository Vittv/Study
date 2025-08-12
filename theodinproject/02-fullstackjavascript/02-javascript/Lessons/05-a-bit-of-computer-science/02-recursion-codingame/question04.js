// Write a function called all which accepts an array and a callback and returns true if every value in the array returns true when passed as a parameter to the callback function

// Sample:
/*
var allAreLessThanSeven = all([1,2,9], function(num){
	return num < 7;
});

console.log(allAreLessThanSeven); // false
*/

function all(array, callback) {
  let copy = copy || array.slice(); // Shallow copies array

  if (copy.length === 0) return true;

  if (callback(copy[0])) {
    copy.shift(); // Remove first element from array
    return all(copy, callback);
  } else {
    return false;
  }
}