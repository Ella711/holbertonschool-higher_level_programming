#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log('Code:', response.statusCode);
  }
});
