#!/usr/bin/node
const fs = require('fs');

// Get the file paths from the command line arguments
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// Initialize an empty string to hold the data
let data = '';

// Check if the first source file is not empty
if (fs.statSync(fileA).size !== 0) {
  // Read the source file
  const data1 = fs.readFileSync(fileA, 'utf8');
  data += data1 + '\n';
}

// Check if the second source file is not empty
if (fs.statSync(fileB).size !== 0) {
  // Read the source file
  const data2 = fs.readFileSync(fileB, 'utf8');
  data += data2;
}

// Write the concatenated data to the destination file
fs.writeFileSync(fileC, data.trim());

// Print the concatenated data
console.log(data.trim());
