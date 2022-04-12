#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = 18;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const i in results) {
      const characters = results[i].characters;
      for (const chars in characters) {
        if (characters[chars].includes(characterId)) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Error code:' + response.statusCode);
  }
});
