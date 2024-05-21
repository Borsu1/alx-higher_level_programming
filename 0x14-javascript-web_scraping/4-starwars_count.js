#!/usr/bin/node
const axios = require('axios');

async function getMovieTitle (episodeNumber) {
  try {
    const url = `https://swapi.dev/api/films/${episodeNumber}/`;
    const response = await axios.get(url);
    console.log(`Title of Episode ${episodeNumber}: ${response.data.title}`);
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
  }
}

// Example usage:
const episodeToSearch = 4; // Replace with the desired episode number
getMovieTitle(episodeToSearch);
