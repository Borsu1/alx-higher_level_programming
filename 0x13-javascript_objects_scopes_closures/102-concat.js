#!/usr/bin/node
const fs = require('fs');

// Get the file paths from the command line arguments
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

// Initialize an empty string to hold the data
let data = '';

// Check if the first source file is not empty
if (fs.statSync(sourceFile1).size !== 0) {
  // Read the source file
  const data1 = fs.readFileSync(sourceFile1, 'utf8');
  data += data1 + '\n';
}

// Check if the second source file is not empty
if (fs.statSync(sourceFile2).size !== 0) {
  // Read the source file
  const data2 = fs.readFileSync(sourceFile2, 'utf8');
  data += data2;
}

// Write the concatenated data to the destination file
fs.writeFileSync(destinationFile, data);

// Print the concatenated data
console.log(data);
