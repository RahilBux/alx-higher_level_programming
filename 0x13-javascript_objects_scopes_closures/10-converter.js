#!/usr/bin/python3

exports.converter = function (base) {
  return function (n) {
    return n.toString(base);
  };
};
