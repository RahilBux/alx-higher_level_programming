#!/usr/bin/node

exports.callmeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
};
