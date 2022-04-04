#!/usr/bin/node

const factNum = parseInt(process.argv[2]);

function recursiveFactorial (factNum) {
  if (factNum < 1 || isNaN(factNum)) {
    return 1;
  } else {
    return factNum * recursiveFactorial(factNum - 1);
  }
}

console.log(recursiveFactorial(factNum));
