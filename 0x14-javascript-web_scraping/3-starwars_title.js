#!/usr/bin/node

const request = require('request')
const movieId = process.argv[2]
const starWarsAPI = `https://swapi-api.alx-tools.com/api/films/${movieId}`

request.get(starWarsAPI, (error, response, body) => {
  // console.log('Must print movie')
  if (response.statusCode === 200) {
    const movie = JSON.parse(body)
    console.log(movie.title)
  } else {
    console.error(error)
  }
  // console.log('Must print error');
  // if (response.statusCode !== 200) {
  //  console.error(`Error: ${response.statusCode}`)
  // }
  // const movie  = JSON.parse(body);
  // console.log(movie.title);
})
