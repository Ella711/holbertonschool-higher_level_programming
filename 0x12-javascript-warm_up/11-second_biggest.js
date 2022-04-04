#!/usr/bin/node

const argsArray = process.argv.slice(2);

if (argsArray.length < 2) {
  console.log(0);
} else {
  argsArray.sort((x, y) => x - y);
  argsArray.pop();
  console.log(argsArray.pop());
}
