#!/usr/bin/node
// Import the `list` array from the '100-data.js' module
const { list } = require('./100-data.js');

// Create a new list where each value is the product of the corresponding value in the initial list and its index
const newList = list.map((value, index) => value * index);

// Log the initial list to the console
console.log(list);

// Log the new list to the console
console.log(newList);
