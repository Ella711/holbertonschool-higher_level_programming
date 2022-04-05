#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i = 0;

    if (c === undefined) {
      this.print();
    } else {
      while (i < this.width) {
        console.log(c.repeat(this.height));
        i++;
      }
    }
  }
};
