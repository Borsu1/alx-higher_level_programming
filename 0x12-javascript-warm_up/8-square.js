#!/usr/bin/node
const size = process.argv[2];
const num = Number(size);

if (Number.isInteger(num)) {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
} else {
  console.log('Missing size');
}
