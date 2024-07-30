#!/usr/bin/node
/*
const request = require('request');

const id = process.argv[2];

const starWarsAPI = `https://swapi-api.alx-tools.com/api/films/${id}`;

//if (!movieID) {
//	console.error('Movie not found')i
//}

request(starWarsAPI, (err, response, body) => {
	if (err){
		console.error(err);
		return;
	}

	if (response.statusCode !== 200) {
		console.error(`Error: ${response.statusCode}`);
		return;
	}

	const movie = JSON.parse(body);
	console.log(movie.title)
});
*/

const request = require('request');
const movie_id = process.argv[2];
const star_wars_api = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;

request.get(star_wars_api, (error, response, body) => {
        //console.log('Must print movie')
	if (response.statusCode === 200) {
		const movie = JSON.parse(body);
		console.log(movie.title);
	}
	//console.log('Must print error');
        if (response.statusCode !== 200) {
                console.error(`Error: ${response.statusCode}`);
                return;
        }
        //const movie  = JSON.parse(body);
        //console.log(movie.title);
});

