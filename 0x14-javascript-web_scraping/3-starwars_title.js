#!/usr/bin/node
// Import the request module for making HTTP requests
const request = require('request');

// Get the movie ID from command line arguments
// process.argv[0] is 'node'
// process.argv[1] is the script name
// process.argv[2] is our first actual argument (movie ID)
if (process.argv.length < 3) {
  console.error('Usage: node <script-file> <ID>');
  process.exit(1);
}

const movieId = process.argv[2];

// Construct the API URL with the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  // Handle network errors
  if (error) {
    console.error('Error making request:', error);
    process.exit(1);
  }

  // Parse the JSON string to object
  try {
    // Parse the JSON response body
    const movie = JSON.parse(body);
    // Print only the movie title
    console.log(movie.title);
  } catch (error) {
    // Handle JSON parsing errors
    console.error('Error parsing body:', error);
  }
});
