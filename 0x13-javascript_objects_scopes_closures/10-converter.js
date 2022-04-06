#!/usr/bin/node

// exports.converter = (base) => (num) => num.toString(base);
exports.converter = function (base) {
  function convert (num) {
    return num.toString(base);
  }
  return convert;
};
