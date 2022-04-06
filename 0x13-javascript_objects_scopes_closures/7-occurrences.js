#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let occurrences = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      occurrences += 1;
    }
    i++;
  }
  return occurrences;
};
