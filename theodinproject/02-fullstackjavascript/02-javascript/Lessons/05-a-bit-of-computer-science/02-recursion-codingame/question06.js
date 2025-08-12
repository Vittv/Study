// Write a function called contains that searches for a value in a nested object. It returns true if the object contains that value.

// Sample:
/*
var nestedObject = {
    data: {
        info: {
            stuff: {
                thing: {
                    moreStuff: {
                        magicNumber: 44,
                        something: 'foo2'
                    }
                }
            }
        }
    }
}

let hasIt = contains(nestedObject, 44); // true
let doesntHaveIt = contains(nestedObject, "foo"); // false
*/

function contains(object, searchValue) {
  if (typeof object !== "object" || object === null) {
    return object === searchValue;
  }

  for (const value of Object.values(object)) {
    if (contains(value, searchValue)) {
      return true;
    }
  }
  return false;
}