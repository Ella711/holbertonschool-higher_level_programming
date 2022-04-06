#!/usr/bin/node

const dict = require('./101-data').dict;

const sortDict = {};
for (const key in dict) {
  if (sortDict[dict[key]] === undefined) {
    sortDict[dict[key]] = [];
  }
  sortDict[dict[key]].push(key);
}
console.log(sortDict);
