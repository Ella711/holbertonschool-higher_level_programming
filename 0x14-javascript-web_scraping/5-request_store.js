#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => (error)
  ? console.log(error)
  : fs.writeFile(file, body, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  }));
