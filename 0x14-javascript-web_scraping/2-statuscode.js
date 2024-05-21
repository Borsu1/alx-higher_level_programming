#!/usr/bin/node
const axios = require('axios');

async function getStatus (url) {
  try {
    const response = await axios.get(url);
    console.log(`code: ${response.status}`);
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
  }
}

// Example usage:
const urlToRequest = 'https://example.com'; // Replace with your desired URL
getStatus(urlToRequest);
