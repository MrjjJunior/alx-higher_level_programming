#!/usr/bin/node

const request = require('request');
const requestURL = process.argv[2];

request(requestURL, (err, response, body) => {
	if (err) {
		console.error(err);
		return;
	}

	console.log(`code: ${response.statusCode}`);
});

