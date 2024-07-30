#!/usr/bin/node

const request = require('request')

const apiURL = process.argv[2]

request(apiURL, function (error, response, body) {
  if (response.statusCode === 200) {
    const todos = JSON.parse(body)
    const completed = {}
    todos.forEach((todo) => {
      if (todo.completed) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1
        } else {
          completed[todo.userId]++
        }
      }
    })
    const output = `{${Object.entries(completed).map(([key, value]) => ` '${key}': ${value}`).join(',\n ')} }`
    console.log(Object.keys(completed).length > 2 ? output : completed)
  } else {
    console.error(error)
    return
  }
})
