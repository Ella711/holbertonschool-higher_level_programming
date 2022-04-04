#!/usr/bin/node

const firstInt = parseInt(process.argv[2]);
const secondInt = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

if (firstInt && secondInt) {
  console.log(add(firstInt, secondInt));
} else {
  console.log(NaN);
}
