#!/usr/bin/node

const fs = require('fs');
const process = require('process');

// Get the file path and string from the arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Check if both file path and content are provided
if (!filePath || !content) {
  console.error('Usage: node 1-writeme.js <file_path> "<string_to_write>"');
  process.exit(1);
}

// Write the string to the file in UFT-8 encoding
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    // Print the error object if an error occurs
    console.error(err);
  } else {
    // Print a sucess message
    console.log('String written to ' + filePath);
  }
});
