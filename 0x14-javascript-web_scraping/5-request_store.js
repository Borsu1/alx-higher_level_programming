#!/usr/bin/node
const fs = require('fs');
const axios = require('axios');

async function fetchAndSave (url, filePath) {
  try {
    const response = await axios.get(url);
    const content = response.data;

    // Write the content to the specified file
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log(`Web content saved to ${filePath}`);
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
  }
}

// Example usage:
const urlToRequest = 'https://example.com'; // Replace with your desired URL
const outputPath = 'output.txt'; // Replace with your desired file path
fetchAndSave(urlToRequest, outputPath);
