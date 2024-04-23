#!/usr/bin/node

// Import the built-in Node.js 'fs' module
const fs = require('fs');

// Import the 'request' module
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

// Use the 'request' module to perform an HTTP GET request to the URL
request(url).pipe(fs.createWriteStream(filePath));


