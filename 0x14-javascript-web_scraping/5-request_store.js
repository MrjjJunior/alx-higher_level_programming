#!/usr/bin/node

const fs = require('fs')
const request = require('request')
const urlRequest = process.argv[2]
const filePath = process.argv[3]

request(urlRequest).pipe(fs.createWriteStream(filePath))
