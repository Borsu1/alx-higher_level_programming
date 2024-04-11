#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is not a positive integer, create an empty object
      this.width = undefined;
      this.height = undefined;
    }
  }
}
module.exports = Rectangle;
