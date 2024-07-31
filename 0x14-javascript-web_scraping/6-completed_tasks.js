#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const mydic = {};

request(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    const response = JSON.parse(body);

    for (let i = 0; i < response.length; i++) {
      if (response[i].completed === true) {
        if (mydic[response[i].userId] === undefined) {
          mydic[response[i].userId] = 1;
	} else {
          mydic[response[i].userId] += 1;
	}
      }
    }
  }
  console.log(mydic);
});
