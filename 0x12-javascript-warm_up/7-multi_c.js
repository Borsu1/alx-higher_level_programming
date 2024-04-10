#!/usr/bin/node
const x = process.argv[2];
const num = Number(x);

if (Number.isInteger(num)) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
