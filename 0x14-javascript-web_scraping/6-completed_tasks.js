#!/usr/bin/node
const axios = require('axios');

async function countCompletedTasks (apiUrl) {
  try {
    const response = await axios.get(apiUrl);
    const todos = response.data;

    // Create a map to track completed tasks per user
    const completedTasksByUser = new Map();

    // Count completed tasks
    todos.forEach((todo) => {
      if (todo.completed) {
        const userId = todo.userId;
        completedTasksByUser.set(userId, (completedTasksByUser.get(userId) || 0) + 1);
      }
    });

    // Print the results
    completedTasksByUser.forEach((count, userId) => {
      console.log(`User ${userId} completed ${count} tasks.`);
    });
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
  }
}

// Example usage:
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';
countCompletedTasks(apiUrl);
