#!/usr/bin/node
const axios = require('axios');

async function getCharactersForMovie (movieId) {
  try {
    const url = `https://swapi.dev/api/films/${movieId}/`;
    const response = await axios.get(url);
    const characters = response.data.characters;

    for (const characterUrl of characters) {
      const characterResponse = await axios.get(characterUrl);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
  }
}

// Example usage:
const movieIdToSearch = 3; // Replace with the desired movie ID
getCharactersForMovie(movieIdToSearch);
