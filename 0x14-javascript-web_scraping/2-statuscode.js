#!/usr/bin/node

const request = require('request');

// Get the URL from the first argument
const url = process.argv[2];

// Check if the URL is provided

if (!url) {
  console.error('Usage: node 2-statuscode.js <URL>');
  process.exit(1);
}

// Make GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    // Print the error object if an error occurs
    console.error('Error:', error);
  } else {
    // Print the status code
    console.log(`code: ${response.statusCode}`);
  }
});
