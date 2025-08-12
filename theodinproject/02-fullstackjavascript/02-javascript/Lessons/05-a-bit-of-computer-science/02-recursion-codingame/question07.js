// Given a multi-dimensional integer array, return the total number of integers stored inside this array

// Sample: 
// var seven = totalIntegers([[[5], 3], 0, 2, ['foo'], [], [4, [5, 6]]]); // 7

function totalIntegers(array){
	if(array.length === 0) return 0;

	let total = 0;
	let first = array.shift();

	if (Array.isArray(first)){
		total += totalIntegers(first); 
	} else if (Number.isInteger(first)) {
		total += 1;
	}

	return total + totalIntegers(array);
}