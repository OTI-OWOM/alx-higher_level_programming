#!/usr/bin/node

const fs = require('fs');

<<<<<<< HEAD
// Check if the file path argument is provided
if (process.argv.length < 3) {
	  console.error('Usage: node read-file.js <file-path>');
	  process.exit(1);
=======
// Get the file path from the first argument
const filePath = process.argv[2];

// Check if the file path is provided
if (!filePath) {
  console.error('usage: node 0-readme.js <file_path>');
  process.exit(1);
>>>>>>> d812f16f378fca67ff63f4c3297f11c5ef273c5e
}

// Get the file path from command line arguments
const filePath = process.argv[2];

// Read the file in UTF-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
<<<<<<< HEAD
	 if (err) {
		 console.error(err);
	 } else {
		console.log(data);
	}
=======
  if (err) {
    // Print the error object if an error occurs
    console.error(err);
  } else {
    // print the file content
    console.log(data);
  }
>>>>>>> d812f16f378fca67ff63f4c3297f11c5ef273c5e
});
