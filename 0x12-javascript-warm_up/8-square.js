#!/usr/bin/node

const argument = parseInt(process.argv[2]);
let i = 0;

if (isNaN(argument)) {
  console.log('Missing size');
} else {
  while (i < argument) {
    console.log('X'.repeat(argument));
    i++;
  }
}
