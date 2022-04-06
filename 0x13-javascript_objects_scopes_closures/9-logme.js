#!/usr/bin/node

let index = 0;
exports.logMe = (item) => console.log((index++) + ': ' + item);
