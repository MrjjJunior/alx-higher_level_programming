#!/usr/bin/node

const request = require('request')

const api_url = process.argv[2];

request(api_url, function (error, response, body)) {
	if (response.statusCode === 200) {
		const todos = JSON.parse

