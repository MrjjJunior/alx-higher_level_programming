#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url_to_request = process.argv[2];
const file_path_to_store = process.argv[3];

request(url_to_request).pipe(fs.createWriteStream(file_path_to_store));

