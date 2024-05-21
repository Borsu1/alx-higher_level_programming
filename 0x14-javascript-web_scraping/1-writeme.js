#!/usr/bin/node
const fs = require('fs');

function writeToFile (filePath, content) {
  try {
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log(`Content successfully written to ${filePath}`);
  } catch (error) {
    console.error(`Error writing to the file: ${error.message}`);
  }
}

// Usage example:
const filePath = process.argv[2];
const content = process.argv[3];
writeToFile(filePath, content);
