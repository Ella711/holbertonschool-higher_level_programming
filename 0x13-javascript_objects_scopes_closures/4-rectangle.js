#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      return undefined;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let i = 0;

    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }

  rotate () {
    const tempWidth = this.width;

    this.width = this.height;
    this.height = tempWidth;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
