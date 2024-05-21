#!/usr/bin/node

function readAndPrintFile (filePath) {
  const fs = require('fs');

  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    console.log(content);
  } catch (error) {
    console.error(`Error reading the file: ${error.message}`);
  }
}

if (require.main === module) {
  if (process.argv.length !== 3) {
    console.error('Usage: node 0-readme.js <file_path>');
  } else {
    const filePath = process.argv[2];
    readAndPrintFile(filePath);
  }
}
