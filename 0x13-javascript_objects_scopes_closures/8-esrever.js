#!/usr/bin/node

exports.esrever = function (list) {
  let start = 0;
  let end = list.length - 1;
  while (start < end) {
    const tempStart = list[start];
    list[start] = list[end];
    list[end] = tempStart;
    start++; end--;
  }
  return list;
};
