package main

func Sum(numbers []int) int {
	sum := 0
	// the range function returns the index and the value
	// by using "_", we ignore the index
	for _, number := range numbers {
		sum += number
	}

	return sum
}

// variadic functions ... accept any number of arguments
func SumAll(numbersToSum ...[]int) []int {
	var sums []int
	for _, numbers := range numbersToSum {
		sums = append(sums, Sum(numbers))
	}

	return sums
}

func SumAllTails(numbersToSum ...[]int) []int {
	var sums []int
	for _, numbers := range numbersToSum {
		// in case one of the arrays is empty
		if len(numbers) == 0 {
			sums = append(sums, 0)
		} else {
			// 1: means to take everything from 1 to the end
			tail := numbers[1:]
			sums = append(sums, Sum(tail))
		}
	}

	return sums
}
