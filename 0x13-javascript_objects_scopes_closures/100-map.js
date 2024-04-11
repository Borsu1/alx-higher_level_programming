#!/usr/bin/node
// The array that export a `list` from the file 100-data.js
const { list } = require('./100-data.js');

// Create a new list with each value equal to the value of the initial list, multiplied by the index in the list
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log('Initial list:', list);
console.log('New list:', newList);
