// Write a function called sumRange. It will take a number and then return the sum of all numbers from 1 up to the number passed in.

// Sample: sumRange(3) returns 6, since 1 + 2 + 3 = 6.

const sumRange = (n) => {
  if (n == 1) return 1;
  return n + sumRange(n - 1);
}