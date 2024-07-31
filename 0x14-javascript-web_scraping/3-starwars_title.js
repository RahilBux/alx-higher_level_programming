#!/usr/bin/node

const request = require('request');
const end = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request({ url: end, methods: 'GET' }, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(body && JSON.parse(body).title);
  }
});
