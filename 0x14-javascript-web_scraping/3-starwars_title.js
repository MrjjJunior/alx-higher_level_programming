#!/usr/bin/node

const request = require('request');
const movie_id = process.argv[2];
const star_wars_api = 'https://swapi-api.alx-tools.com/api/films/:id' + movie_id;

//request.get(star_wars_api, (error, response, body) => {
//	if (error) {
//		console.error(error);
//		return;
//	}
//	if (response.statusCode !== 200) {
//		console.error('Error: ${response.statusCode}');
//		return;
//	}
//	const movie  = JSON.parse(body);
//	console.log(movie.title);
//});

request(star_wars_api, function(error, response, body){
	console.log(error || JSON.parse(body).title);
});
