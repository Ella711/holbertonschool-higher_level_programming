#!/usr/bin/node

const cLang = 'C is fun';
let i = 0;

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  while (i < parseInt(process.argv[2])) {
    console.log(cLang);
    i++;
  }
}
