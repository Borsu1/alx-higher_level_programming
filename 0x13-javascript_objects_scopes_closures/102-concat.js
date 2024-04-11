#!/usr/bin/node
const fs = require('fs');

// Get the file paths from the command line arguments
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

// Read the source files
const data1 = fs.readFileSync(sourceFile1, 'utf8');
const data2 = fs.readFileSync(sourceFile2, 'utf8');

// Concatenate the data from the source files
const data = data1 + data2;

// Write the concatenated data to the destination file
fs.writeFileSync(destinationFile, data);

console.log('Files have been concatenated successfully.');
