// Tasks
// 1 - Translate border-left-width to borderLeftWidth
// Write the function camelize(str) that changes dash-separated words like “my-short-string” into camel-cased “myShortString”.
// That is: removes all dashes, each word after dash becomes uppercased.

function camelize(str) {
    return str
        .split('-') // splits 'my-long-word' into array ['my', 'long', 'word']
        .map(
            // capitalizes first letters of all array items except the first one
            // converts ['my', 'long', 'word'] into ['my', 'Long', 'Word']    
            (word, index) => index == 0 ? word : word[0].toUpperCase() + word.slice(1)
        )
        .join('') // joins ['my', 'Long', 'Word'] into 'myLongWord'
};

camelize("background-color") // == 'backgroundColor';
camelize("list-style-image") //  == 'listStyleImage';
camelize("-webkit-transition") // == 'WebkitTransition';

// 2 - Filter range
// Write a function filterRange(arr, a, b) that gets an array arr, looks for elements with values higher or equal to a and lower or equal to b and return a result as an array.

// The function should not modify the array. It should return the new array.

function filterRange(arr, a, b) {
    return arr.filter(item => (a <= item && item <= b));    
}

let arr = [5, 3, 8, 1];

let filtered = filterRange(arr, 1, 4);

alert( filtered ); // 3, 1 (matching values)
alert( arr ) // 5, 3, 8, 1 (not modified)

// 3 - Filter range "in place"
// Write a function filterRangeInPlace(arr, a, b) that gets any array arr and removes from it all values except those that are between a and b. The test is: a <= arr[i] <= b.

// The function should only mofidy the array. It should not return anything.

function filterRangeInPlace(arr, a, b) { 
    for (let i = 0; i < arr.length; i++) {
        let val == arr[i];

        // remove if outside of the interval
        if (val < a || val > b) {
            arr.splice(i, 1);
            i--;
        }
    }
};

let arr = [5, 3, 8, 1];

filterRangeInPlace(arr, 1, 4); // removed the numbers except from 1 to 4
alert( arr ); // [3, 1]

// 4 - Sort in decreasing order

let arr = [5, 2, 1, -10, 8]
arr.sort((a, b) => b - a);
alert( arr );

// 5 - Copy and sort array
// We have an array of strings arr. We'd like to have a sorted copy of it, but keep arr unmodified.
// Create a function copySorted(arr) that returns such a copy.

function copySorted(arr) {
    return arr.slice().sort();
}

let arr = ["HTML", "JavaScript", "CSS"];

let sorted = copySorted(arr);

alert( sorted ); // CSS, HTML, JavaScript
alert( arr ); // HTML, JavaScript, CSS (no changes)

// 6 - Map to names
// You have an array of user objects, each one has user.name. Write the code that converts it into an array of names.

let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 28 };

let users = [ john, pete, mary ];

let names = users.map(item => item.name);
alert( names ); // John, Pete, Mary

// 7 - Map to objects
// You have an array of user objects, each one has name, surname, and id.
// Write the code to create another array from it, of objects with id and fullName, where fullName is generated from name and surname

let john = { name: "John", surname: "Smith", id: 1 };
let pete = { name: "Pete", surname: "Hunt", id: 2 };
let mary = { name: "Mary", surname: "Key", id: 3 };

let users = [ john, pete, mary ];

let usersMapped = users.map(user => ({
  fullName: `${user.name} ${user.surname}`,
  id: user.id
}));

/*
usersMapped = [
  { fullName: "John Smith", id: 1 },
  { fullName: "Pete Hunt", id: 2 },
  { fullName: "Mary Key", id: 3 }
]
*/

alert( usersMapped[0].id ); // 1
alert( usersMapped[0].fullName ); // John Smith

// 8 - Sort users by age
// Write the function sortByAge(users) that gets an array of objects with the age propertyand sorts them by age.

function sortByAge(arr) {
    arr.sort((a, b) => a.age - b.age);
  }
  
let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 28 };

let arr = [ pete, john, mary ];

sortByAge(arr);

// now sorted is: [john, mary, pete]
alert(arr[0].name); // John
alert(arr[1].name); // Mary
alert(arr[2].name); // Pete

// 9 - Shuffle an array
// Write the function shuffle(array) that shuffles (randomly reorders) elements of the array.
// Multiple runs of shuffle may lead to different orders of elements. For instance:
// All element orders should have an equal probability. For instance, [1,2,3] can be reordered as [1,2,3] or [1,3,2] or [3,1,2] etc, with equal probability of each case.

function shuffle(array) {
array.sort(() => Math.random() - 0.5);
}

let arr = [1, 2, 3];
shuffle(arr);
alert(arr);

// 10 - Get average age
// Write the function getAverageAge(users) that gets an array of objects with property age and returns the average age.
// The formula for the average is (age1 + age2 + ... + ageN) / N.

function getAverageAge(users) {
return users.reduce((prev, user) => prev + user.age, 0) / users.length;
}

let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 29 };

let arr = [ john, pete, mary ];

alert( getAverageAge(arr) ); // 28

// 11 - Filter unique array members
// Let arr be an array.
// Create a function unique(arr) that should return an array with unique items of arr.

function unique(arr) {
let result = [];

for (let str of arr) {
    if (!result.includes(str)) {
    result.push(str);
    }
}

return result;
}

let strings = ["Hare", "Krishna", "Hare", "Krishna",
"Krishna", "Krishna", "Hare", "Hare", ":-O"
];

alert( unique(strings) ); // Hare, Krishna, :-O  

// 12 - Create keyed object from array
// Let's say we received an array of users in the form {id:..., name:..., age:... }.
// Create a function groupById(arr) that creates an object from it, with id as the key, and array items as values.

function groupById(array) {
    return array.reduce((obj, value) => {
      obj[value.id] = value;
      return obj;
    }, {})
  }