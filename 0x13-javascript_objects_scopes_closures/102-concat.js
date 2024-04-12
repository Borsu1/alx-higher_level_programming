#!/usr/bin/node
const fs = require('fs');

function concatFiles(file1, file2, dest) {
    const data1 = fs.readFileSync(file1, 'utf8');
    const data2 = fs.readFileSync(file2, 'utf8');
    fs.writeFileSync(dest, data1 + data2);
}

if (process.argv.length !== 5) {
    console.log("Usage: node concatFiles.js <file1> <file2> <destination>");
} else {
    concatFiles(process.argv[2], process.argv[3], process.argv[4]);
}
