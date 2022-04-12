#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const tasksDict = {};
    for (const i in tasks) {
      if (tasks[i].completed) {
        if (!tasksDict[tasks[i].userId]) {
          tasksDict[tasks[i].userId] = 1;
        } else {
          tasksDict[tasks[i].userId]++;
        }
      }
    }
    console.log(tasksDict);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
