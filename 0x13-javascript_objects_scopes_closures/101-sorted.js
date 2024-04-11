#!/usr/bin/node
// The dictionary is exported as `dict` in 101-data.js
const { dict } = require('./101-data.js');

const newDict = {};

// Iterate over each key-value pair in the original dictionary
for (const userId in dict) {
  const occurrence = dict[userId];

  // If this occurrence has not been seen before, initialize an empty array for it
  if (!newDict[occurrence]) {
    newDict[occurrence] = [];
  }

  // Add the user id to the list of user ids for this occurrence
  newDict[occurrence].push(userId);
}

// Print the new dictionary
console.log(newDict);
