#!/usr/bin/node

const fs = require('fs');
const process = require('process');

// Get the file path from the first argument
const filePath = process.argv[2];

// Check if the file path is provided
if (!filePath) {
  console.error('usage: node 0-readme.js <file_path>');
  process.exit(1);
}

// Read thr file in UTF-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
// Print the error object if an error occurs
    console.error(err);
  } else {
// print the file content
    console.log(data);
  }
});
