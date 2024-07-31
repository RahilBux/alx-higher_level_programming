#!/usr/bin/node

const f = require('fs');
f.writeFile(process.argv[2], process.argv[3], err => {
  if (err) {
    console.log(err);
  }
});
